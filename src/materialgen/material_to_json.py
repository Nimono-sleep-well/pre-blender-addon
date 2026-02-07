import bpy
import mathutils
import bpy_types
import json

all_nodes = [
    "ShaderNodeAddShader",
    "ShaderNodeAmbientOcclusion",
    "ShaderNodeAttribute",
    "ShaderNodeBackground",
    "ShaderNodeBevel",
    "ShaderNodeBlackbody",
    "ShaderNodeBrightContrast",
    "ShaderNodeBsdfAnisotropic",
    "ShaderNodeBsdfDiffuse",
    "ShaderNodeBsdfGlass",
    "ShaderNodeBsdfHair",
    "ShaderNodeBsdfHairPrincipled",
    "ShaderNodeBsdfMetallic",
    "ShaderNodeBsdfPrincipled",
    "ShaderNodeBsdfRayPortal",
    "ShaderNodeBsdfRefraction",
    "ShaderNodeBsdfSheen",
    "ShaderNodeBsdfToon",
    "ShaderNodeBsdfTranslucent",
    "ShaderNodeBsdfTransparent",
    "ShaderNodeBump",
    "ShaderNodeCameraData",
    "ShaderNodeClamp",
    "ShaderNodeCombineColor",
    "ShaderNodeCombineXYZ",
    "ShaderNodeCustomGroup",
    "ShaderNodeDisplacement",
    "ShaderNodeEeveeSpecular",
    "ShaderNodeEmission",
    "ShaderNodeFloatCurve",
    "ShaderNodeFresnel",
    "ShaderNodeGamma",
    "ShaderNodeGroup",
    "ShaderNodeHairInfo",
    "ShaderNodeHoldout",
    "ShaderNodeHueSaturation",
    "ShaderNodeInvert",
    "ShaderNodeLayerWeight",
    "ShaderNodeLightFalloff",
    "ShaderNodeLightPath",
    "ShaderNodeMapRange",
    "ShaderNodeMapping",
    "ShaderNodeMath",
    "ShaderNodeMix",
    "ShaderNodeMixRGB",
    "ShaderNodeMixShader",
    "ShaderNodeNewGeometry",
    "ShaderNodeNormal",
    "ShaderNodeNormalMap",
    "ShaderNodeObjectInfo",
    "ShaderNodeOutputAOV",
    "ShaderNodeOutputLight",
    "ShaderNodeOutputLineStyle",
    "ShaderNodeOutputMaterial",
    "ShaderNodeOutputWorld",
    "ShaderNodeParticleInfo",
    "ShaderNodePointInfo",
    "ShaderNodeRGB",
    "ShaderNodeRGBCurve",
    "ShaderNodeRGBToBW",
    "ShaderNodeRadialTiling",
    "ShaderNodeScript",
    "ShaderNodeSeparateColor",
    "ShaderNodeSeparateXYZ",
    "ShaderNodeShaderToRGB",
    "ShaderNodeSqueeze",
    "ShaderNodeSubsurfaceScattering",
    "ShaderNodeTangent",
    "ShaderNodeTexBrick",
    "ShaderNodeTexChecker",
    "ShaderNodeTexCoord",
    "ShaderNodeTexEnvironment",
    "ShaderNodeTexGabor",
    "ShaderNodeTexGradient",
    "ShaderNodeTexIES",
    "ShaderNodeTexImage",
    "ShaderNodeTexMagic",
    "ShaderNodeTexNoise",
    "ShaderNodeTexSky",
    "ShaderNodeTexVoronoi",
    "ShaderNodeTexWave",
    "ShaderNodeTexWhiteNoise",
    "ShaderNodeUVAlongStroke",
    "ShaderNodeUVMap",
    "ShaderNodeValToRGB",
    "ShaderNodeValue",
    "ShaderNodeVectorCurve",
    "ShaderNodeVectorDisplacement",
    "ShaderNodeVectorMath",
    "ShaderNodeVectorRotate",
    "ShaderNodeVectorTransform",
    "ShaderNodeVertexColor",
    "ShaderNodeVolumeAbsorption",
    "ShaderNodeVolumeCoefficients",
    "ShaderNodeVolumeInfo",
    "ShaderNodeVolumePrincipled",
    "ShaderNodeVolumeScatter",
    "ShaderNodeWavelength",
    "ShaderNodeWireframe",
]

### Function ###


### Create Material Data
def createMaterialData(input_name: str = "Material") -> bpy.types.Material:
    mtl_data = bpy.data.materials.new(input_name)
    mtl_data.use_fake_user = True
    mtl_data.use_nodes = True
    for node in mtl_data.node_tree.nodes:
        mtl_data.node_tree.nodes.remove(node)
    return mtl_data
    # Input:
    # input_name = "NewMaterial"
    # Output:
    # <bpy_struct, Material("NewMaterial") at 0x0000013BC27A7408>


### Set Default Shader Node
def extractShaderNodeData(
    input_mtl_data: bpy.types.Material, node_type: str
) -> bpy.types.Material:
    node_tree = input_mtl_data.node_tree
    nodes = node_tree.nodes
    temp_node = nodes.new(type=node_type)
    print(temp_node.inputs.name)

    return input_mtl_data
    # Input:
    # input_mtl_data = <bpy_struct, Material("NewMaterial") at 0x0000013BC2EA6C88>
    # Output:
    # <bpy_struct, Material("NewMaterial") at 0x0000013BC2EA6C88>


### Print Material Data
def bpyPrintMaterialData(input_mtl_data: bpy.types.Material):
    print(f"Material: {input_mtl_data} {type(input_mtl_data)}")
    print(
        f"- Nodes: {[node_data.name for node_data in input_mtl_data.node_tree.nodes]}"
    )
    print(
        f"- Links: {[[link_data.from_node.name, link_data.to_node.name] for link_data in input_mtl_data.node_tree.links]}"
    )
    # Input:
    # input_mtl_data = <bpy_struct, Material("NewMaterial") at 0x0000013BC2EA6C88>
    # Output:
    # Material: <bpy_struct, Material("NewMaterial") at 0x0000013BC2EA6C88> <class 'bpy.types.Material'>
    # - Nodes: ['Material Output', 'Principled BSDF']
    # - Links: [['Principled BSDF', 'Material Output']]


### Main ###

if __name__ == "__main__":

    material_nodes_data = {}

    ### Create Data
    mtl_data = createMaterialData("NewMaterial")

    ### Set Data
    for node in all_nodes:
        mtl_doc = extractShaderNodeData(mtl_data, node)

    ### Print Data
    bpyPrintMaterialData(mtl_data)
    # Material: <bpy_struct, Material("NewMaterial") at 0x0000013BC2EA6C88> <class 'bpy.types.Material'>
    # - Nodes: ['Material Output', 'Principled BSDF']
    # - Links: [['Principled BSDF', 'Material Output']]
