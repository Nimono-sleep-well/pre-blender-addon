bl_info = {
    "name": "Text Input Material Addon",
    "author": "Your Name",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Text Input Tab",
    "description": "Create material whose name comes from text input",
    "category": "3D View",
}

import bpy


# アドオン全体で共有するプロパティ
class MyAddonProperties(bpy.types.PropertyGroup):
    user_text: bpy.props.StringProperty(
        name="Text", description="Input material name here", default=""
    )


# テキストをコンソールに出力するオペレーター（前回のまま）
class MYADDON_OT_print_text(bpy.types.Operator):
    bl_idname = "myaddon.print_text"
    bl_label = "Print Text"
    bl_description = "Print the input text to the console"

    def execute(self, context):
        props = context.scene.my_addon_props
        self.report({"INFO"}, f"Input text: {props.user_text}")
        print("Input text:", props.user_text)
        return {"FINISHED"}


# 入力テキストを名前とするマテリアルを作成するオペレーター
class MYADDON_OT_create_material(bpy.types.Operator):
    bl_idname = "myaddon.create_material"
    bl_label = "Create Material"
    bl_description = "Create a material whose name is the input text"

    def execute(self, context):
        props = context.scene.my_addon_props
        name = props.user_text.strip()

        # 空文字チェック
        if not name:
            self.report(
                {"WARNING"}, "テキストが空です。マテリアル名を入力してください。"
            )
            return {"CANCELLED"}

        # すでに同名マテリアルが存在するか確認
        mat = bpy.data.materials.get(name)
        if mat is None:
            mat = bpy.data.materials.new(name=name)
            self.report({"INFO"}, f"マテリアル '{name}' を作成しました。")
        else:
            self.report(
                {"INFO"}, f"マテリアル '{name}' はすでに存在するため再利用します。"
            )

        # ここで必要なら、アクティブオブジェクトへ割り当てる処理も可能です
        # obj = context.active_object
        # if obj is not None:
        #     if obj.data and hasattr(obj.data, "materials"):
        #         if obj.data.materials:
        #             obj.data.materials[0] = mat
        #         else:
        #             obj.data.materials.append(mat)

        return {"FINISHED"}


# UI パネル
class MYADDON_PT_panel(bpy.types.Panel):
    bl_label = "Text Input Material"
    bl_idname = "MYADDON_PT_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Text Input Tab"  # Nパネルのタブ名

    def draw(self, context):
        layout = self.layout
        props = context.scene.my_addon_props

        # テキスト入力欄
        layout.prop(props, "user_text", text="Material Name")

        # ボタン群
        row = layout.row()
        row.operator("myaddon.print_text", text="Print to Console")
        row = layout.row()
        row.operator("myaddon.create_material", text="Create Material")


classes = (
    MyAddonProperties,
    MYADDON_OT_print_text,
    MYADDON_OT_create_material,
    MYADDON_PT_panel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.my_addon_props = bpy.props.PointerProperty(type=MyAddonProperties)


def unregister():
    del bpy.types.Scene.my_addon_props

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
