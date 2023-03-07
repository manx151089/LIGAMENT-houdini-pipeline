# Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/obj")

# Code for /obj/example_deformer
hou_node = hou_parent.createNode("geo", "example_deformer", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(0, 0))
hou_node.setSelectableInViewport(True)
hou_node.showOrigin(False)
hou_node.useXray(False)
hou_node.setDisplayFlag(True)
hou_node.hide(False)
hou_node.setSelected(True)

hou_parm_template_group = hou.ParmTemplateGroup()
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("stdswitcher4", "Transform", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("xOrd", "Transform Order", menu_items=(["srt","str","rst","rts","tsr","trs"]), menu_labels=(["Scale Rot Trans","Scale Trans Rot","Rot Scale Trans","Rot Trans Scale","Trans Scale Rot","Trans Rot Scale"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template2.setJoinWithNext(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("rOrd", "Rotate Order", menu_items=(["xyz","xzy","yxz","yzx","zxy","zyx"]), menu_labels=(["Rx Ry Rz","Rx Rz Ry","Ry Rx Rz","Ry Rz Rx","Rz Rx Ry","Rz Ry Rx"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template2.hideLabel(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("t", "Translate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 0)", "script_action_help": "Select an object to match the translation with.", "script_action_icon": "BUTTONS_match_transform"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("r", "Rotate", 3, default_value=([0, 0, 0]), min=0, max=360, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 1)", "script_action_help": "Select an object to match the rotation with.", "script_action_icon": "BUTTONS_match_rotation"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("s", "Scale", 3, default_value=([1, 1, 1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 2)", "script_action_help": "Select an object to match the scale with.", "script_action_icon": "BUTTONS_match_scale"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("p", "Pivot Translate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.setTags({"script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 3)", "script_action_help": "Select an object to match the pivot with.", "script_action_icon": "BUTTONS_match_pivot"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("pr", "Pivot Rotate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.setTags({"script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 4)", "script_action_help": "Select an object to match the pivot rotation with.", "script_action_icon": "BUTTONS_match_pivot_rotation"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("scale", "Uniform Scale", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("pre_xform", "Modify Pre-Transform", menu_items=(["clean","cleantrans","cleanrot","cleanscales","extract","reset"]), menu_labels=(["Clean Transform","Clean Translates","Clean Rotates","Clean Scales","Extract Pre-transform","Reset Pre-transform"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("keeppos", "Keep Position When Parenting", default_value=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("childcomp", "Child Compensation", default_value=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("constraints_on", "Enable Constraints", default_value=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("constraints_path", "Constraints", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ constraints_on == 0 }")
hou_parm_template2.setTags({"opfilter": "!!CHOP", "oprelative": ".", "script_action": "import objecttoolutils\nobjecttoolutils.constraintsMenu(kwargs)", "script_action_help": "", "script_action_icon": "BUTTONS_add_constraints"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("lookatpath", "Look At", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.hide(True)
hou_parm_template2.setTags({"opfilter": "!!OBJ!!", "oprelative": "."})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("lookupobjpath", "Look Up Object", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.hide(True)
hou_parm_template2.setTags({"opfilter": "!!OBJ!!", "oprelative": "."})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("lookup", "Look At Up Vector", 1, default_value=(["on"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["off","on","quat","pos","obj"]), menu_labels=(["Don't Use Up Vector","Use Up Vector","Use Quaternions","Use Global Position","Use Up Object"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("pathobjpath", "Path Object", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.hide(True)
hou_parm_template2.setTags({"opfilter": "!!SOP!!", "oprelative": "."})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("roll", "Roll", 1, default_value=([0]), min=-360, max=360, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Angle, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("pos", "Position", 1, default_value=([0]), min=0, max=10, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("uparmtype", "Parameterization", menu_items=(["uniform","arc"]), menu_labels=(["Uniform","Arc Length"]), default_value=1, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("pathorient", "Orient Along Path", 1, default_value=([1]), min=0, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("up", "Orient Up Vector", 3, default_value=([0, 1, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Vector, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("bank", "Auto-Bank factor", 1, default_value=([0]), min=-1, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("stdswitcher4_1", "Render", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("shop_materialpath", "Material", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"opfilter": "!!CUSTOM/MATERIAL!!", "oprelative": "."})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("shop_materialopts", "Options", menu_items=([]), menu_labels=([]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Mini, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("tdisplay", "Display", default_value=False)
hou_parm_template2.hideLabel(True)
hou_parm_template2.setJoinWithNext(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("display", "Display", 1, default_value=([1]), min=0, max=1, min_is_strict=True, max_is_strict=True, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("viewportlod", "Display As", menu_items=(["full","points","box","centroid","hidden","subd"]), menu_labels=(["Full Geometry","Point Cloud","Bounding Box","Centroid","Hidden","Subdivision Surface / Curves"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template2.setHelp("Choose how the object's geometry should be rendered in the viewport")
hou_parm_template2.setTags({"spare_category": "Render"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vm_rendervisibility", "Render Visibility", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["*","primary","primary|shadow","-primary","-diffuse","-diffuse&-reflect&-refract",""]), menu_labels=(["Visible to all","Visible only to primary rays","Visible only to primary and shadow rays","Invisible to primary rays (Phantom)","Invisible to diffuse rays","Invisible to secondary rays","Invisible (Unrenderable)"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace)
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "rendervisibility", "spare_category": "Render"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vm_rendersubd", "Render Polygons As Subdivision (Mantra)", default_value=False)
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "rendersubd", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vm_subdstyle", "Subdivision Style", 1, default_value=(["mantra_catclark"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["mantra_catclark","osd_catclark"]), menu_labels=(["Mantra Catmull-Clark","OpenSubdiv Catmull-Clark"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 }")
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "subdstyle", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vm_subdgroup", "Subdivision Group", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 }")
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "subdgroup", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("vm_osd_quality", "Open Subdiv Quality", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 vm_subdstyle != osd_catclark }")
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "osd_quality", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("vm_osd_vtxinterp", "OSD Vtx Interp", 1, default_value=([2]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["No vertex interpolation","Edges only","Edges and Corners"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 vm_subdstyle != osd_catclark }")
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "osd_vtxinterp", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("vm_osd_fvarinterp", "OSD FVar Interp", 1, default_value=([4]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2","3","4","5"]), menu_labels=(["Smooth everywhere","Sharpen corners only","Sharpen edges and corners","Sharpen edges and propagated corners","Sharpen all boundaries","Bilinear interpolation"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 vm_subdstyle != osd_catclark }")
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "osd_fvarinterp", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("folder0", "Shading", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("categories", "Categories", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setHelp("A list of tags which can be used to select the object")
hou_parm_template3.setTags({"spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("reflectmask", "Reflection Mask", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReferenceList, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setHelp("Objects that will be reflected on this object.")
hou_parm_template3.setTags({"opexpand": "1", "opfilter": "!!OBJ/GEOMETRY!!", "oprelative": "/obj", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("refractmask", "Refraction Mask", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReferenceList, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setHelp("Objects that will be refracted on this object.")
hou_parm_template3.setTags({"opexpand": "1", "opfilter": "!!OBJ/GEOMETRY!!", "oprelative": "/obj", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("lightmask", "Light Mask", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReferenceList, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setHelp("Lights that illuminate this object.")
hou_parm_template3.setTags({"opexpand": "1", "opfilter": "!!OBJ/LIGHT!!", "oprelative": "/obj", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("lightcategories", "Light Selection", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("vm_lpetag", "LPE Tag", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "lpetag", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("vm_volumefilter", "Volume Filter", 1, default_value=(["box"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["box","gaussian","bartlett","catrom","hanning","blackman","sinc"]), menu_labels=(["Box Filter","Gaussian","Bartlett (triangle)","Catmull-Rom","Hanning","Blackman","Sinc (sharpening)"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "filter", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.FloatParmTemplate("vm_volumefilterwidth", "Volume Filter Width", 1, default_value=([1]), min=0.001, max=5, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "filterwidth", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_matte", "Matte shading", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "matte", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_rayshade", "Raytrace Shading", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "rayshade", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("folder0_1", "Sampling", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template3 = hou.MenuParmTemplate("geo_velocityblur", "Geometry Velocity Blur", menu_items=(["off","on","accelblur"]), menu_labels=(["No Velocity Blur","Velocity Blur","Acceleration Blur"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template3.setConditional(hou.parmCondType.DisableWhen, "{ allowmotionblur == 0 }")
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("geo_accelattribute", "Acceleration Attribute", 1, default_value=(["accel"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setConditional(hou.parmCondType.HideWhen, "{ geo_velocityblur != accelblur }")
hou_parm_template3.setTags({"spare_category": "Sampling"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("folder0_2", "Dicing", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template3 = hou.FloatParmTemplate("vm_shadingquality", "Shading Quality", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "shadingquality", "spare_category": "Dicing"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.FloatParmTemplate("vm_flatness", "Dicing Flatness", 1, default_value=([0.05]), min=0, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "flatness", "spare_category": "Dicing"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.IntParmTemplate("vm_raypredice", "Ray Predicing", 1, default_value=([0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["Disable Predicing","Full Predicing","Precompute Bounds"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "raypredice", "spare_category": "Dicing"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_curvesurface", "Shade Curves As Surfaces", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "curvesurface", "spare_category": "Dicing"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("folder0_3", "Geometry", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_rmbackface", "Backface Removal", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "rmbackface", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("shop_geometrypath", "Procedural Shader", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"opfilter": "!!SHOP/GEOMETRY!!", "oprelative": ".", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_forcegeometry", "Force Procedural Geometry Output", default_value=True)
hou_parm_template3.setTags({"spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_rendersubdcurves", "Render Polygon Curves As Subdivision (Mantra)", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "rendersubdcurves", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.IntParmTemplate("vm_renderpoints", "Render As Points (Mantra)", 1, default_value=([2]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["No Point Rendering","Render Only Points","Render Unconnected Points"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "renderpoints", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.IntParmTemplate("vm_renderpointsas", "Render Points As (Mantra)", 1, default_value=([0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1"]), menu_labels=(["Spheres","Circles"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template3.setConditional(hou.parmCondType.DisableWhen, "{ vm_renderpoints == 0 }")
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "renderpointsas", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_usenforpoints", "Use N For Point Rendering", default_value=False)
hou_parm_template3.setConditional(hou.parmCondType.DisableWhen, "{ vm_renderpoints == 0 }")
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "usenforpoints", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.FloatParmTemplate("vm_pointscale", "Point Scale", 1, default_value=([1]), min=0, max=10, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template3.setConditional(hou.parmCondType.DisableWhen, "{ vm_renderpoints == 0 }")
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "pointscale", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_pscalediameter", "Treat Point Scale as Diameter Instead of Radius", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "pscalediameter", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_metavolume", "Metaballs as Volume", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "metavolume", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.IntParmTemplate("vm_coving", "Coving", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["Disable Coving","Coving for displacement/sub-d","Coving for all primitives"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "coving", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("vm_materialoverride", "Material Override", 1, default_value=(["compact"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["none","full","compact"]), menu_labels=(["Disabled","Evaluate for Each Primitve/Point","Evaluate Once"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_overridedetail", "Ignore Geometry Attribute Shaders", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "overridedetail", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_procuseroottransform", "Proc Use Root Transform", default_value=True)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "procuseroottransform", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("stdswitcher4_2", "Misc", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("use_dcolor", "Set Wireframe Color", default_value=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("dcolor", "Wireframe Color", 3, default_value=([1, 1, 1]), min=0, max=1, min_is_strict=True, max_is_strict=True, look=hou.parmLook.ColorSquare, naming_scheme=hou.parmNamingScheme.RGBA)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("picking", "Viewport Selecting Enabled", default_value=True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("pickscript", "Select Script", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.FileReference, file_type=hou.fileType.Any, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace)
hou_parm_template2.setTags({"filechooser_mode": "read"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("caching", "Cache Object Transform", default_value=True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vport_shadeopen", "Shade Open Curves In Viewport", default_value=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vport_displayassubdiv", "Display as Subdivision in Viewport", default_value=False)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("vport_onionskin", "Onion Skinning", menu_items=(["off","xform","on"]), menu_labels=(["Off","Transform only","Full Deformation"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
hou_node.setParmTemplateGroup(hou_parm_template_group)
# Code for /obj/example_deformer/stdswitcher1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("stdswitcher1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/xOrd parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("xOrd")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("srt")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/rOrd parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("rOrd")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("xyz")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((True, True, True))


# Code for /obj/example_deformer/r parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm_tuple = hou_node.parmTuple("r")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((True, True, True))


# Code for /obj/example_deformer/s parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm_tuple = hou_node.parmTuple("s")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((1, 1, 1))
hou_parm_tuple.setAutoscope((True, True, True))


# Code for /obj/example_deformer/p parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm_tuple = hou_node.parmTuple("p")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/example_deformer/pr parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm_tuple = hou_node.parmTuple("pr")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/example_deformer/scale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("scale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pre_xform parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("pre_xform")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("clean")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/keeppos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("keeppos")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/childcomp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("childcomp")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/constraints_on parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("constraints_on")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/constraints_path parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("constraints_path")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/lookatpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("lookatpath")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/lookupobjpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("lookupobjpath")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/lookup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("lookup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("on")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pathobjpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("pathobjpath")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/roll parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("roll")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("pos")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/uparmtype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("uparmtype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("arc")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pathorient parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("pathorient")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/up parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm_tuple = hou_node.parmTuple("up")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 1, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/example_deformer/bank parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("bank")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/shop_materialpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("shop_materialpath")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/shop_materialopts parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("shop_materialopts")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("override")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/tdisplay parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("tdisplay")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/display parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("display")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/use_dcolor parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("use_dcolor")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/dcolor parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm_tuple = hou_node.parmTuple("dcolor")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((1, 1, 1))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/example_deformer/picking parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("picking")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pickscript parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("pickscript")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/caching parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("caching")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vport_shadeopen parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vport_shadeopen")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vport_displayassubdiv parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vport_displayassubdiv")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vport_onionskin parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vport_onionskin")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("off")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/stdswitcher41 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("stdswitcher41")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/viewportlod parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("viewportlod")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("full")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_rendervisibility parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_rendervisibility")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_rendersubd parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_rendersubd")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_subdstyle parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_subdstyle")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("mantra_catclark")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_subdgroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_subdgroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_osd_quality parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_osd_quality")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_osd_vtxinterp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_osd_vtxinterp")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(2)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_osd_fvarinterp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_osd_fvarinterp")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(4)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/folder01 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("folder01")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/categories parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("categories")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/reflectmask parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("reflectmask")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/refractmask parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("refractmask")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/lightmask parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("lightmask")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/lightcategories parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("lightcategories")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_lpetag parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_lpetag")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_volumefilter parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_volumefilter")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("box")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_volumefilterwidth parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_volumefilterwidth")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_matte parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_matte")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_rayshade parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_rayshade")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/geo_velocityblur parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("geo_velocityblur")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("off")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/geo_accelattribute parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("geo_accelattribute")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("accel")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_shadingquality parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_shadingquality")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_flatness parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_flatness")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.050000000000000003)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_raypredice parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_raypredice")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_curvesurface parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_curvesurface")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_rmbackface parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_rmbackface")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/shop_geometrypath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("shop_geometrypath")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_forcegeometry parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_forcegeometry")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_rendersubdcurves parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_rendersubdcurves")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_renderpoints parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_renderpoints")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(2)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_renderpointsas parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_renderpointsas")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_usenforpoints parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_usenforpoints")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_pointscale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_pointscale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_pscalediameter parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_pscalediameter")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_metavolume parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_metavolume")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_coving parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_coving")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_materialoverride parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_materialoverride")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("compact")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_overridedetail parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_overridedetail")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/vm_procuseroottransform parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer")
hou_parm = hou_node.parm("vm_procuseroottransform")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___toolid___", "sop_grid")
hou_node.setUserData("___Version___", "19.5.493")
hou_node.setUserData("___toolcount___", "1")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.5.493")
# Update the parent node.
hou_parent = hou_node

# Code for /obj/example_deformer/grid1
hou_node = hou_parent.createNode("grid", "grid1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.65882, -0.558824))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(True)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/example_deformer/grid1/type parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/grid1")
hou_parm = hou_node.parm("type")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("poly")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/grid1/surftype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/grid1")
hou_parm = hou_node.parm("surftype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("quads")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/grid1/orient parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/grid1")
hou_parm = hou_node.parm("orient")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("zx")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/grid1/size parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/grid1")
hou_parm_tuple = hou_node.parmTuple("size")
hou_parm_tuple.lock((False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((10, 10))
hou_parm_tuple.setAutoscope((False, False))


# Code for /obj/example_deformer/grid1/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/grid1")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/example_deformer/grid1/r parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/grid1")
hou_parm_tuple = hou_node.parmTuple("r")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/example_deformer/grid1/rows parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/grid1")
hou_parm = hou_node.parm("rows")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/grid1/cols parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/grid1")
hou_parm = hou_node.parm("cols")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/grid1/orderu parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/grid1")
hou_parm = hou_node.parm("orderu")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(4)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/grid1/orderv parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/grid1")
hou_parm = hou_node.parm("orderv")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(4)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/grid1/interpu parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/grid1")
hou_parm = hou_node.parm("interpu")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/grid1/interpv parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/grid1")
hou_parm = hou_node.parm("interpv")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___toolid___", "sop_grid")
hou_node.setUserData("___Version___", "19.5.493")
hou_node.setUserData("___toolcount___", "1")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.5.493")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/example_deformer/grid2
hou_node = hou_parent.createNode("grid", "grid2", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(0.852941, -0.558824))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/example_deformer/grid2/type parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/grid2")
hou_parm = hou_node.parm("type")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("poly")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/grid2/surftype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/grid2")
hou_parm = hou_node.parm("surftype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("quads")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/grid2/orient parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/grid2")
hou_parm = hou_node.parm("orient")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("zx")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/grid2/size parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/grid2")
hou_parm_tuple = hou_node.parmTuple("size")
hou_parm_tuple.lock((False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((3.7393990919237963, 5.2626900000000001))
hou_parm_tuple.setAutoscope((False, False))


# Code for /obj/example_deformer/grid2/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/grid2")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0.43581494877604077, 0.035171204629944552, -0.53224745392799377))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/example_deformer/grid2/r parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/grid2")
hou_parm_tuple = hou_node.parmTuple("r")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 17.087335744945584))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/example_deformer/grid2/rows parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/grid2")
hou_parm = hou_node.parm("rows")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(3)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/grid2/cols parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/grid2")
hou_parm = hou_node.parm("cols")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(4)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/grid2/orderu parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/grid2")
hou_parm = hou_node.parm("orderu")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(4)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/grid2/orderv parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/grid2")
hou_parm = hou_node.parm("orderv")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(4)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/grid2/interpu parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/grid2")
hou_parm = hou_node.parm("interpu")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/grid2/interpv parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/grid2")
hou_parm = hou_node.parm("interpv")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.5.493")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.5.493")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/example_deformer/deltamush1
hou_node = hou_parent.createNode("deltamush", "deltamush1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(1.19412, -1.55882))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/example_deformer/deltamush1/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/deltamush1")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/deltamush1/method parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/deltamush1")
hou_parm = hou_node.parm("method")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("uniform")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/deltamush1/iterations parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/deltamush1")
hou_parm = hou_node.parm("iterations")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/deltamush1/stepsize parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/deltamush1")
hou_parm = hou_node.parm("stepsize")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.70099999999999996)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/deltamush1/pinborder parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/deltamush1")
hou_parm = hou_node.parm("pinborder")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/deltamush1/updateaffectednmls parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/deltamush1")
hou_parm = hou_node.parm("updateaffectednmls")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/deltamush1/clampstepsize parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/deltamush1")
hou_parm = hou_node.parm("clampstepsize")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.5.493")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.5.493")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/example_deformer/scatter1
hou_node = hou_parent.createNode("scatter::2.0", "scatter1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.84118, -1.55882))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/example_deformer/scatter1/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/stdswitcher1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("stdswitcher1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/generateby parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("generateby")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("bydensity")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/indepvoxel parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("indepvoxel")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/forcetotal parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("forcetotal")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/npts parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("npts")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1000)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/densityscale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("densityscale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/usedensityattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("usedensityattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/densityattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("densityattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("density")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/useareaattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("useareaattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/areaattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("areaattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("area")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/useareaforvolumes parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("useareaforvolumes")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/usedensitytexture parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("usedensitytexture")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/densitytexture parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("densitytexture")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("default.pic")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/uvattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("uvattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("uv")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/primcountattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("primcountattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("count")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/useemergencylimit parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("useemergencylimit")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/emergencylimit parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("emergencylimit")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1000000)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/seed parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("seed")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/overrideprimseed parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("overrideprimseed")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/primseedattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("primseedattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("primid")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/randomizeorder parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("randomizeorder")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/relaxpoints parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("relaxpoints")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/relaxiterations parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("relaxiterations")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/scaleradiiby parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("scaleradiiby")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/usemaxradius parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("usemaxradius")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/maxradius parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("maxradius")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/useprimnumattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("useprimnumattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/primnumattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("primnumattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("sourceprim")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/useprimuvwattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("useprimuvwattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/primuvwattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("primuvwattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("sourceprimuv")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/useoutputdensityattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("useoutputdensityattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/outputdensityattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("outputdensityattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("density")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/useoutputradiusattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("useoutputradiusattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/outputradiusattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("outputradiusattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("pscale")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/radiusintexturespace parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("radiusintexturespace")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/pointattribs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("pointattribs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/vertattribs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("vertattribs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("N uv*")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/primattribs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("primattribs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/scatter1/detailattribs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/scatter1")
hou_parm = hou_node.parm("detailattribs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.5.493")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.5.493")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/example_deformer/copytopoints1
hou_node = hou_parent.createNode("copytopoints::2.0", "copytopoints1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-0.888235, -2.7))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/example_deformer/copytopoints1/sourcegroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/copytopoints1")
hou_parm = hou_node.parm("sourcegroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/copytopoints1/sourcegrouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/copytopoints1")
hou_parm = hou_node.parm("sourcegrouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/copytopoints1/targetgroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/copytopoints1")
hou_parm = hou_node.parm("targetgroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/copytopoints1/useidattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/copytopoints1")
hou_parm = hou_node.parm("useidattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/copytopoints1/idattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/copytopoints1")
hou_parm = hou_node.parm("idattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("name")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/copytopoints1/pack parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/copytopoints1")
hou_parm = hou_node.parm("pack")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/copytopoints1/pivot parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/copytopoints1")
hou_parm = hou_node.parm("pivot")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("centroid")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/copytopoints1/viewportlod parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/copytopoints1")
hou_parm = hou_node.parm("viewportlod")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("full")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/copytopoints1/transform parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/copytopoints1")
hou_parm = hou_node.parm("transform")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/copytopoints1/useimplicitn parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/copytopoints1")
hou_parm = hou_node.parm("useimplicitn")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/copytopoints1/resettargetattribs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/copytopoints1")
hou_parm = hou_node.parm("resettargetattribs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("0")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/copytopoints1/targetattribs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/copytopoints1")
hou_parm = hou_node.parm("targetattribs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(3)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/copytopoints1/useapply1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/copytopoints1")
hou_parm = hou_node.parm("useapply1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/copytopoints1/applyto1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/copytopoints1")
hou_parm = hou_node.parm("applyto1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("points")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/copytopoints1/applymethod1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/copytopoints1")
hou_parm = hou_node.parm("applymethod1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("copy")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/copytopoints1/applyattribs1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/copytopoints1")
hou_parm = hou_node.parm("applyattribs1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*,^v,^Alpha,^N,^up,^pscale,^scale,^orient,^rot,^pivot,^trans,^transform")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/copytopoints1/useapply2 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/copytopoints1")
hou_parm = hou_node.parm("useapply2")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/copytopoints1/applyto2 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/copytopoints1")
hou_parm = hou_node.parm("applyto2")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("points")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/copytopoints1/applymethod2 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/copytopoints1")
hou_parm = hou_node.parm("applymethod2")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("mult")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/copytopoints1/applyattribs2 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/copytopoints1")
hou_parm = hou_node.parm("applyattribs2")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("Alpha")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/copytopoints1/useapply3 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/copytopoints1")
hou_parm = hou_node.parm("useapply3")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/copytopoints1/applyto3 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/copytopoints1")
hou_parm = hou_node.parm("applyto3")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("points")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/copytopoints1/applymethod3 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/copytopoints1")
hou_parm = hou_node.parm("applymethod3")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("add")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/copytopoints1/applyattribs3 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/copytopoints1")
hou_parm = hou_node.parm("applyattribs3")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("v")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.5.493")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.5.493")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/example_deformer/pointwrangle1
hou_node = hou_parent.createNode("attribwrangle", "pointwrangle1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(0.156341, -9.34954))
hou_node.bypass(False)
hou_node.setDisplayFlag(True)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(True)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/example_deformer/pointwrangle1/folder01 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pointwrangle1")
hou_parm = hou_node.parm("folder01")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pointwrangle1/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pointwrangle1")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pointwrangle1/grouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pointwrangle1")
hou_parm = hou_node.parm("grouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pointwrangle1/class parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pointwrangle1")
hou_parm = hou_node.parm("class")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("point")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pointwrangle1/vex_numcount parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pointwrangle1")
hou_parm = hou_node.parm("vex_numcount")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pointwrangle1/vex_threadjobsize parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pointwrangle1")
hou_parm = hou_node.parm("vex_threadjobsize")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1024)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pointwrangle1/snippet parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pointwrangle1")
hou_parm = hou_node.parm("snippet")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("matrix packedtrf =primintrinsic(1,\"packedfulltransform\",0);\nv@Cd.x=f@sel;\n//packedtrf=invert(packedtrf);\nmatrix id =ident();\nv@P*=slerp(id,packedtrf,@sel);")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pointwrangle1/exportlist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pointwrangle1")
hou_parm = hou_node.parm("exportlist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pointwrangle1/vex_strict parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pointwrangle1")
hou_parm = hou_node.parm("vex_strict")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pointwrangle1/autobind parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pointwrangle1")
hou_parm = hou_node.parm("autobind")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pointwrangle1/bindings parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pointwrangle1")
hou_parm = hou_node.parm("bindings")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pointwrangle1/groupautobind parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pointwrangle1")
hou_parm = hou_node.parm("groupautobind")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pointwrangle1/groupbindings parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pointwrangle1")
hou_parm = hou_node.parm("groupbindings")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pointwrangle1/vex_cwdpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pointwrangle1")
hou_parm = hou_node.parm("vex_cwdpath")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(".")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pointwrangle1/vex_outputmask parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pointwrangle1")
hou_parm = hou_node.parm("vex_outputmask")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pointwrangle1/vex_updatenmls parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pointwrangle1")
hou_parm = hou_node.parm("vex_updatenmls")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pointwrangle1/vex_matchattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pointwrangle1")
hou_parm = hou_node.parm("vex_matchattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("id")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pointwrangle1/vex_inplace parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pointwrangle1")
hou_parm = hou_node.parm("vex_inplace")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pointwrangle1/vex_selectiongroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pointwrangle1")
hou_parm = hou_node.parm("vex_selectiongroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pointwrangle1/vex_precision parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pointwrangle1")
hou_parm = hou_node.parm("vex_precision")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("auto")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/example_deformer/box1
hou_node = hou_parent.createNode("box", "box1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(0.723529, -3.99412))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/example_deformer/box1/type parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/box1")
hou_parm = hou_node.parm("type")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("polymesh")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/box1/surftype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/box1")
hou_parm = hou_node.parm("surftype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("quads")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/box1/consolidatepts parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/box1")
hou_parm = hou_node.parm("consolidatepts")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/box1/size parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/box1")
hou_parm_tuple = hou_node.parmTuple("size")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((1, 1, 1))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/example_deformer/box1/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/box1")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/example_deformer/box1/r parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/box1")
hou_parm_tuple = hou_node.parmTuple("r")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/example_deformer/box1/scale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/box1")
hou_parm = hou_node.parm("scale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/box1/divrate parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/box1")
hou_parm_tuple = hou_node.parmTuple("divrate")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((2, 2, 2))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/example_deformer/box1/orderrate parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/box1")
hou_parm_tuple = hou_node.parmTuple("orderrate")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((4, 4, 4))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/example_deformer/box1/dodivs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/box1")
hou_parm = hou_node.parm("dodivs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/box1/divs parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/box1")
hou_parm_tuple = hou_node.parmTuple("divs")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((3, 3, 3))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/example_deformer/box1/rebar parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/box1")
hou_parm = hou_node.parm("rebar")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/box1/orientedbbox parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/box1")
hou_parm = hou_node.parm("orientedbbox")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/box1/vertexnormals parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/box1")
hou_parm = hou_node.parm("vertexnormals")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.5.493")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.5.493")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/example_deformer/pack1
hou_node = hou_parent.createNode("pack", "pack1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(0.725629, -4.89329))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/example_deformer/pack1/viewportlod parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pack1")
hou_parm = hou_node.parm("viewportlod")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("full")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pack1/createpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pack1")
hou_parm = hou_node.parm("createpath")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pack1/path parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pack1")
hou_parm = hou_node.parm("path")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("op:`opfullpath('.')`")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pack1/packbyname parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pack1")
hou_parm = hou_node.parm("packbyname")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pack1/nameattribute parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pack1")
hou_parm = hou_node.parm("nameattribute")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("name")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pack1/packedfragments parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pack1")
hou_parm = hou_node.parm("packedfragments")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pack1/pivot parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pack1")
hou_parm = hou_node.parm("pivot")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("centroid")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pack1/transfer_attributes parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pack1")
hou_parm = hou_node.parm("transfer_attributes")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/pack1/transfer_groups parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/pack1")
hou_parm = hou_node.parm("transfer_groups")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.5.493")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.5.493")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/example_deformer/transform1
hou_node = hou_parent.createNode("xform", "transform1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(0.196132, -5.92479))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/example_deformer/transform1/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/transform1/grouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm = hou_node.parm("grouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/transform1/xOrd parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm = hou_node.parm("xOrd")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("srt")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/transform1/rOrd parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm = hou_node.parm("rOrd")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("xyz")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/transform1/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((True, True, True))


# Code for /obj/example_deformer/transform1/r parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm_tuple = hou_node.parmTuple("r")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0.00085074656945962202, -0.081740974632439956, -0.59630368608109163))
hou_parm_tuple.setAutoscope((True, True, True))


# Code for /obj/example_deformer/transform1/s parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm_tuple = hou_node.parmTuple("s")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((1, 1, 1))
hou_parm_tuple.setAutoscope((True, True, True))


# Code for /obj/example_deformer/transform1/shear parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm_tuple = hou_node.parmTuple("shear")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/example_deformer/transform1/scale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm = hou_node.parm("scale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/transform1/parmgroup_pivotxform parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm = hou_node.parm("parmgroup_pivotxform")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/transform1/p parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm_tuple = hou_node.parmTuple("p")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/example_deformer/transform1/pr parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm_tuple = hou_node.parmTuple("pr")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/example_deformer/transform1/parmgroup_prexform parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm = hou_node.parm("parmgroup_prexform")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/transform1/prexform_xOrd parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm = hou_node.parm("prexform_xOrd")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("srt")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/transform1/prexform_rOrd parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm = hou_node.parm("prexform_rOrd")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("xyz")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/transform1/prexform_t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm_tuple = hou_node.parmTuple("prexform_t")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/example_deformer/transform1/prexform_r parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm_tuple = hou_node.parmTuple("prexform_r")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/example_deformer/transform1/prexform_s parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm_tuple = hou_node.parmTuple("prexform_s")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((1, 1, 1))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/example_deformer/transform1/prexform_shear parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm_tuple = hou_node.parmTuple("prexform_shear")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/example_deformer/transform1/movecentroid parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm = hou_node.parm("movecentroid")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("0")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/transform1/attribs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm = hou_node.parm("attribs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/transform1/updatenmls parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm = hou_node.parm("updatenmls")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/transform1/updateaffectednmls parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm = hou_node.parm("updateaffectednmls")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/transform1/vlength parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm = hou_node.parm("vlength")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/transform1/invertxform parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm = hou_node.parm("invertxform")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/transform1/addattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm = hou_node.parm("addattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/transform1/outputattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm = hou_node.parm("outputattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("xform")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/transform1/outputmerge parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/transform1")
hou_parm = hou_node.parm("outputmerge")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("post")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.5.493")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.5.493")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/example_deformer/attribtransfer1
hou_node = hou_parent.createNode("attribtransfer", "attribtransfer1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.49267, -8.00259))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/example_deformer/attribtransfer1/srcgroups parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/attribtransfer1")
hou_parm = hou_node.parm("srcgroups")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/attribtransfer1/srcgrouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/attribtransfer1")
hou_parm = hou_node.parm("srcgrouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("primitive")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/attribtransfer1/dstgroups parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/attribtransfer1")
hou_parm = hou_node.parm("dstgroups")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/attribtransfer1/dstgrouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/attribtransfer1")
hou_parm = hou_node.parm("dstgrouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("primitive")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/attribtransfer1/cardswitcher1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/attribtransfer1")
hou_parm = hou_node.parm("cardswitcher1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/attribtransfer1/detailattribs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/attribtransfer1")
hou_parm = hou_node.parm("detailattribs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/attribtransfer1/detailattriblist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/attribtransfer1")
hou_parm = hou_node.parm("detailattriblist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/attribtransfer1/primitiveattribs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/attribtransfer1")
hou_parm = hou_node.parm("primitiveattribs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/attribtransfer1/primattriblist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/attribtransfer1")
hou_parm = hou_node.parm("primattriblist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/attribtransfer1/pointattribs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/attribtransfer1")
hou_parm = hou_node.parm("pointattribs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/attribtransfer1/pointattriblist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/attribtransfer1")
hou_parm = hou_node.parm("pointattriblist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/attribtransfer1/vertexattribs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/attribtransfer1")
hou_parm = hou_node.parm("vertexattribs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/attribtransfer1/vertexattriblist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/attribtransfer1")
hou_parm = hou_node.parm("vertexattriblist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/attribtransfer1/copyvariable parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/attribtransfer1")
hou_parm = hou_node.parm("copyvariable")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/attribtransfer1/matchpattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/attribtransfer1")
hou_parm = hou_node.parm("matchpattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/attribtransfer1/kernel parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/attribtransfer1")
hou_parm = hou_node.parm("kernel")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("elendt")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/attribtransfer1/kernelradius parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/attribtransfer1")
hou_parm = hou_node.parm("kernelradius")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/attribtransfer1/maxsamplecount parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/attribtransfer1")
hou_parm = hou_node.parm("maxsamplecount")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/attribtransfer1/threshold parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/attribtransfer1")
hou_parm = hou_node.parm("threshold")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/attribtransfer1/thresholddist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/attribtransfer1")
hou_parm = hou_node.parm("thresholddist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.42999999999999999)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/attribtransfer1/blendwidth parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/attribtransfer1")
hou_parm = hou_node.parm("blendwidth")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(2)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/attribtransfer1/uniformbias parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/attribtransfer1")
hou_parm = hou_node.parm("uniformbias")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.5.493")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.5.493")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/example_deformer/createsel
hou_node = hou_parent.createNode("attribwrangle", "createsel", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-3.19338, -6.96469))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/example_deformer/createsel/folder01 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel")
hou_parm = hou_node.parm("folder01")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel/grouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel")
hou_parm = hou_node.parm("grouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel/class parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel")
hou_parm = hou_node.parm("class")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("point")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel/vex_numcount parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel")
hou_parm = hou_node.parm("vex_numcount")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel/vex_threadjobsize parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel")
hou_parm = hou_node.parm("vex_threadjobsize")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1024)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel/snippet parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel")
hou_parm = hou_node.parm("snippet")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("f@sel = 0;")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel/exportlist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel")
hou_parm = hou_node.parm("exportlist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel/vex_strict parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel")
hou_parm = hou_node.parm("vex_strict")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel/autobind parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel")
hou_parm = hou_node.parm("autobind")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel/bindings parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel")
hou_parm = hou_node.parm("bindings")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel/groupautobind parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel")
hou_parm = hou_node.parm("groupautobind")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel/groupbindings parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel")
hou_parm = hou_node.parm("groupbindings")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel/vex_cwdpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel")
hou_parm = hou_node.parm("vex_cwdpath")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(".")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel/vex_outputmask parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel")
hou_parm = hou_node.parm("vex_outputmask")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel/vex_updatenmls parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel")
hou_parm = hou_node.parm("vex_updatenmls")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel/vex_matchattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel")
hou_parm = hou_node.parm("vex_matchattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("id")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel/vex_inplace parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel")
hou_parm = hou_node.parm("vex_inplace")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel/vex_selectiongroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel")
hou_parm = hou_node.parm("vex_selectiongroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel/vex_precision parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel")
hou_parm = hou_node.parm("vex_precision")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("auto")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/example_deformer/createsel1
hou_node = hou_parent.createNode("attribwrangle", "createsel1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-0.84159, -6.96469))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/example_deformer/createsel1/folder01 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel1")
hou_parm = hou_node.parm("folder01")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel1/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel1")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel1/grouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel1")
hou_parm = hou_node.parm("grouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel1/class parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel1")
hou_parm = hou_node.parm("class")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("point")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel1/vex_numcount parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel1")
hou_parm = hou_node.parm("vex_numcount")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel1/vex_threadjobsize parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel1")
hou_parm = hou_node.parm("vex_threadjobsize")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1024)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel1/snippet parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel1")
hou_parm = hou_node.parm("snippet")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("f@sel = 1;")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel1/exportlist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel1")
hou_parm = hou_node.parm("exportlist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel1/vex_strict parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel1")
hou_parm = hou_node.parm("vex_strict")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel1/autobind parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel1")
hou_parm = hou_node.parm("autobind")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel1/bindings parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel1")
hou_parm = hou_node.parm("bindings")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel1/groupautobind parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel1")
hou_parm = hou_node.parm("groupautobind")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel1/groupbindings parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel1")
hou_parm = hou_node.parm("groupbindings")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel1/vex_cwdpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel1")
hou_parm = hou_node.parm("vex_cwdpath")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(".")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel1/vex_outputmask parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel1")
hou_parm = hou_node.parm("vex_outputmask")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel1/vex_updatenmls parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel1")
hou_parm = hou_node.parm("vex_updatenmls")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel1/vex_matchattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel1")
hou_parm = hou_node.parm("vex_matchattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("id")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel1/vex_inplace parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel1")
hou_parm = hou_node.parm("vex_inplace")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel1/vex_selectiongroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel1")
hou_parm = hou_node.parm("vex_selectiongroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/createsel1/vex_precision parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/createsel1")
hou_parm = hou_node.parm("vex_precision")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("auto")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/example_deformer/visualize1
hou_node = hou_parent.createNode("visualize", "visualize1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-3.18148, -9.00259))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

hou_parm_template_group = hou.ParmTemplateGroup()
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("setvisualizers", "Update Visualizers", default_value=False)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("clearvisualizers", "Clear Incoming Visualizers", default_value=False)
hou_parm_template.setConditional(hou.parmCondType.DisableWhen, "{ setvisualizers == 0 }")
hou_parm_template.setTags({"autoscope": "0000000000000000"})
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("wireframe", "Wireframe", menu_items=(["nochange","shaded","viewport","wireframe"]), menu_labels=(["No Change","Force Shaded","Use Viewport Settings","Force Wireframe"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("lit", "Lighting", menu_items=(["nochange","unlit","lit"]), menu_labels=(["No Change","Unlit","Lit"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("xray", "X-Ray", menu_items=(["nochange","disable","enable"]), menu_labels=(["No Change","Disable","Enable"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("setcuspangle", "Set Cusp Angle", default_value=False)
hou_parm_template.hideLabel(True)
hou_parm_template.setJoinWithNext(True)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("cuspangle", "Cusp Angle", 1, default_value=([60]), min=0, max=180, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setConditional(hou.parmCondType.DisableWhen, "{ setcuspangle == 0 }")
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("showpoints", "Show Points", menu_items=(["nochange","unconnected","all"]), menu_labels=(["No Change","Unconnected","All"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("spherepoints", "Points as Spheres", menu_items=(["nochange","disable","enable"]), menu_labels=(["No Change","Disable","Enable"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("spriteblend", "Sprite Blending", menu_items=(["nochange","disable","enable"]), menu_labels=(["No Change","Disable","Enable"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("setspritecutoff", "Set Sprite Cutoff", default_value=False)
hou_parm_template.hideLabel(True)
hou_parm_template.setJoinWithNext(True)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("spritecutoff", "Sprite Cutoff", 1, default_value=([0.5]), min=0, max=1, min_is_strict=True, max_is_strict=True, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setConditional(hou.parmCondType.DisableWhen, "{ setspritecutoff == 0 }")
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("node_vis_enabled", "Visualization Enabled", default_value=True)
hou_parm_template.hide(True)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("num_visualizers", "Visualizers", folder_type=hou.folderType.MultiparmBlock, default_value=0, ends_tab_group=False)
hou_parm_template.hide(True)
hou_parm_template.setTags({"multistartoffset": "0"})
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vis_active#", "Active #", default_value=False)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vis_data#", "Raw Data #", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.hide(True)
hou_parm_template2.hideLabel(True)
hou_parm_template2.setTags({"editor": "1"})
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
hou_node.setParmTemplateGroup(hou_parm_template_group)
# Code for /obj/example_deformer/visualize1/setvisualizers parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/visualize1")
hou_parm = hou_node.parm("setvisualizers")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/visualize1/clearvisualizers parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/visualize1")
hou_parm = hou_node.parm("clearvisualizers")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/visualize1/wireframe parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/visualize1")
hou_parm = hou_node.parm("wireframe")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("nochange")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/visualize1/lit parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/visualize1")
hou_parm = hou_node.parm("lit")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("nochange")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/visualize1/xray parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/visualize1")
hou_parm = hou_node.parm("xray")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("nochange")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/visualize1/setcuspangle parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/visualize1")
hou_parm = hou_node.parm("setcuspangle")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/visualize1/cuspangle parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/visualize1")
hou_parm = hou_node.parm("cuspangle")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(60)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/visualize1/showpoints parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/visualize1")
hou_parm = hou_node.parm("showpoints")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("nochange")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/visualize1/spherepoints parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/visualize1")
hou_parm = hou_node.parm("spherepoints")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("nochange")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/visualize1/spriteblend parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/visualize1")
hou_parm = hou_node.parm("spriteblend")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("nochange")
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/visualize1/setspritecutoff parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/visualize1")
hou_parm = hou_node.parm("setspritecutoff")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/visualize1/spritecutoff parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/visualize1")
hou_parm = hou_node.parm("spritecutoff")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/visualize1/node_vis_enabled parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/visualize1")
hou_parm = hou_node.parm("node_vis_enabled")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/visualize1/num_visualizers parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/visualize1")
hou_parm = hou_node.parm("num_visualizers")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/visualize1/vis_active0 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/visualize1")
hou_parm = hou_node.parm("vis_active0")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/example_deformer/visualize1/vis_data0 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/example_deformer/visualize1")
hou_parm = hou_node.parm("vis_data0")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("{\n\t\"flags\":{\n\t\t\"type\":\"int\",\n\t\t\"value\":27\n\t},\n\t\"icon\":{\n\t\t\"type\":\"string\",\n\t\t\"value\":\"VIEW_visualization_color\"\n\t},\n\t\"label\":{\n\t\t\"type\":\"string\",\n\t\t\"value\":\"Color 1\"\n\t},\n\t\"name\":{\n\t\t\"type\":\"string\",\n\t\t\"value\":\"vis_color_1\"\n\t},\n\t\"parameters\":{\n\t\t\"type\":\"string\",\n\t\t\"value\":\"{\\nversion 0.8\\ncolortype\\t[ 0\\tlocks=0 ]\\t(\\t\\\"attribramped\\\"\\t)\\nclass\\t[ 0\\tlocks=0 ]\\t(\\t\\\"auto\\\"\\t)\\nattrib\\t[ 0\\tlocks=0 ]\\t(\\tsel\\t)\\nuvattrib\\t[ 0\\tlocks=0 ]\\t(\\tuv\\t)\\ndistortiontype\\t[ 0\\tlocks=0 ]\\t(\\t\\\"global\\\"\\t)\\nrangesection\\t[ 0\\tlocks=0 ]\\t(\\t0\\t)\\nrangespec\\t[ 0\\tlocks=0 ]\\t(\\t\\\"min-max\\\"\\t)\\nminscalar\\t[ 0\\tlocks=0 ]\\t(\\t0\\t)\\nmaxscalar\\t[ 0\\tlocks=0 ]\\t(\\t1\\t)\\ncenterscalar\\t[ 0\\tlocks=0 ]\\t(\\t0\\t)\\nwidthscalar\\t[ 0\\tlocks=0 ]\\t(\\t2\\t)\\nclamptype\\t[ 0\\tlocks=0 ]\\t(\\t\\\"edge\\\"\\t)\\nconstcolor\\t[ 0\\tlocks=0 ]\\t(\\t1\\t0\\t0\\t1\\t)\\nusethreevtxcolor\\t[ 0\\tlocks=0 ]\\t(\\t\\\"on\\\"\\t)\\ncolorthreevtx\\t[ 0\\tlocks=0 ]\\t(\\t1\\t1\\t0\\t)\\nusefourvtxcolor\\t[ 0\\tlocks=0 ]\\t(\\t\\\"on\\\"\\t)\\ncolorfourvtx\\t[ 0\\tlocks=0 ]\\t(\\t0.5\\t0.69999999999999996\\t1\\t)\\nusenvtxcolor\\t[ 0\\tlocks=0 ]\\t(\\t\\\"on\\\"\\t)\\ncolornvtx\\t[ 0\\tlocks=0 ]\\t(\\t1\\t0\\t0\\t)\\ntreatasscalar\\t[ 0\\tlocks=0 ]\\t(\\t\\\"on\\\"\\t)\\nusing\\t[ 0\\tlocks=0 ]\\t(\\t\\\"length\\\"\\t)\\ncomponent\\t[ 0\\tlocks=0 ]\\t(\\t0\\t)\\nrefvec\\t[ 0\\tlocks=0 ]\\t(\\t0\\t1\\t0\\t)\\nrandseed\\t[ 0\\tlocks=0 ]\\t(\\t0\\t)\\nvalsep\\t[ 0\\tlocks=0 ]\\t(\\t1\\t)\\nrampsection\\t[ 0\\tlocks=0 ]\\t(\\t0\\t)\\ncolorramppreset\\t[ 0\\tlocks=0 ]\\t(\\t0\\t)\\ncolorramp\\t[ 0\\tlocks=0 ]\\t(\\t4\\t)\\ncolorramp1pos\\t[ 0\\tlocks=0 ]\\t(\\t0\\t)\\ncolorramp1c\\t[ 0\\tlocks=0 ]\\t(\\t0\\t0\\t0\\t)\\ncolorramp1interp\\t[ 0\\tlocks=0 ]\\t(\\t\\\"linear\\\"\\t)\\ncolorramp2pos\\t[ 0\\tlocks=0 ]\\t(\\t0.33333000540733337\\t)\\ncolorramp2c\\t[ 0\\tlocks=0 ]\\t(\\t1\\t0\\t0\\t)\\ncolorramp2interp\\t[ 0\\tlocks=0 ]\\t(\\t\\\"linear\\\"\\t)\\ncolorramp3pos\\t[ 0\\tlocks=0 ]\\t(\\t0.66667002439498901\\t)\\ncolorramp3c\\t[ 0\\tlocks=0 ]\\t(\\t1\\t1\\t0\\t)\\ncolorramp3interp\\t[ 0\\tlocks=0 ]\\t(\\t\\\"linear\\\"\\t)\\ncolorramp4pos\\t[ 0\\tlocks=0 ]\\t(\\t1\\t)\\ncolorramp4c\\t[ 0\\tlocks=0 ]\\t(\\t1\\t1\\t1\\t)\\ncolorramp4interp\\t[ 0\\tlocks=0 ]\\t(\\t\\\"linear\\\"\\t)\\n}\\n\"\n\t},\n\t\"scope\":{\n\t\t\"type\":\"int\",\n\t\t\"value\":2\n\t},\n\t\"type\":{\n\t\t\"type\":\"string\",\n\t\t\"value\":\"vis_color\"\n\t}\n}\n")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code to establish connections for /obj/example_deformer/deltamush1
hou_node = hou_parent.node("deltamush1")
if hou_parent.node("grid2") is not None:
    hou_node.setInput(0, hou_parent.node("grid2"), 0)
# Code to establish connections for /obj/example_deformer/scatter1
hou_node = hou_parent.node("scatter1")
if hou_parent.node("grid1") is not None:
    hou_node.setInput(0, hou_parent.node("grid1"), 0)
# Code to establish connections for /obj/example_deformer/copytopoints1
hou_node = hou_parent.node("copytopoints1")
if hou_parent.node("deltamush1") is not None:
    hou_node.setInput(0, hou_parent.node("deltamush1"), 0)
if hou_parent.node("scatter1") is not None:
    hou_node.setInput(1, hou_parent.node("scatter1"), 0)
# Code to establish connections for /obj/example_deformer/pointwrangle1
hou_node = hou_parent.node("pointwrangle1")
if hou_parent.node("attribtransfer1") is not None:
    hou_node.setInput(0, hou_parent.node("attribtransfer1"), 0)
if hou_parent.node("transform1") is not None:
    hou_node.setInput(1, hou_parent.node("transform1"), 0)
# Code to establish connections for /obj/example_deformer/pack1
hou_node = hou_parent.node("pack1")
if hou_parent.node("box1") is not None:
    hou_node.setInput(0, hou_parent.node("box1"), 0)
# Code to establish connections for /obj/example_deformer/transform1
hou_node = hou_parent.node("transform1")
if hou_parent.node("pack1") is not None:
    hou_node.setInput(0, hou_parent.node("pack1"), 0)
# Code to establish connections for /obj/example_deformer/attribtransfer1
hou_node = hou_parent.node("attribtransfer1")
if hou_parent.node("createsel") is not None:
    hou_node.setInput(0, hou_parent.node("createsel"), 0)
if hou_parent.node("createsel1") is not None:
    hou_node.setInput(1, hou_parent.node("createsel1"), 0)
# Code to establish connections for /obj/example_deformer/createsel
hou_node = hou_parent.node("createsel")
if hou_parent.node("copytopoints1") is not None:
    hou_node.setInput(0, hou_parent.node("copytopoints1"), 0)
# Code to establish connections for /obj/example_deformer/createsel1
hou_node = hou_parent.node("createsel1")
if hou_parent.node("transform1") is not None:
    hou_node.setInput(0, hou_parent.node("transform1"), 0)
# Code to establish connections for /obj/example_deformer/visualize1
hou_node = hou_parent.node("visualize1")
if hou_parent.node("attribtransfer1") is not None:
    hou_node.setInput(0, hou_parent.node("attribtransfer1"), 0)

# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

