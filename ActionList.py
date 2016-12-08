import bpy
# plugin info
bl_info = {
    "name" : "ActionList",
    "author" : "yoshinori.ono",
    "version" : (0, 1),
    "blender" : (2, 7, 4),
    "location" : "PROPERTIES > WINDOW > UIList",
    "location" : "",
    "description" : "ActionList",
    "warning" : "",
    "wiki_url" : "",
    "tracker_url" : "",
    "category" : "User"
}

class ActionList(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        ob = data
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.prop(item, "name", text="", emboss=False, icon_value=icon)
        elif self.layout_type in {'GRID'}:
            pass

class UIListPanelExample(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "ActionList Panel"
    bl_idname = "OBJECT_PT_action_list"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"
    # bl_space_type = 'DOPESHEET_EDITOR'
    # bl_region_type = 'UI'
    # bl_context = "object"

    def draw(self, context):
        layout1 = self.layout
        ob = context.object

        layout2 = self.layout
        ob2 = context.object

        if ob2.animation_data is not None:
            layout2.prop(ob.animation_data, "action")
        else:
            layout2.label("No animation_data.")

        layout1.template_list("ActionList", "", bpy.data, "actions", ob, "action_list_index")

def register():
    bpy.types.Object.action_list_index = bpy.props.IntProperty()
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)
    del bpy.types.Object.action_list_index

if __name__ == "__main__":
    register()
