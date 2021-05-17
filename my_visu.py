# state file generated using paraview version 5.9.0-RC3

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [888, 484]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [40.00709915161133, 19.98710012435913, -0.39749999999999996]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [42.09789640156704, -2.4057983010729864, 11.049527928970207]
renderView1.CameraFocalPoint = [44.722679017685884, 30.761479152692615, -5.725377221249346]
renderView1.CameraViewUp = [0.07814314705829328, 0.44501426108755043, 0.8921075921639314]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 14.119433425026095
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize((888, 484))
path= '/home/Dittu/Documents/Masters/Sem1/GAV/0001/COMBINED_2011013100.nc'

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
nc3 = NetCDFReader(registrationName='nc3', FileName=[path])
nc3.Dimensions = '(Z_MIT40, YC, XG)'
nc3.SphericalCoordinates = 0

# create a new 'Resample To Image'
resampleToImage2 = ResampleToImage(registrationName='ResampleToImage2', Input=nc3)
resampleToImage2.UseInputBounds = 0
resampleToImage2.SamplingDimensions = [500, 500, 50]
resampleToImage2.SamplingBounds = [30.007099151611328, 49.967098236083984, 10.027099609375, 29.98710060119629, -3178.0, -2.0]

# create a new 'NetCDF Reader'
nc2 = NetCDFReader(registrationName='nc2', FileName=[path])
nc2.Dimensions = '(Z_MIT40, YC, XC)'
nc2.SphericalCoordinates = 0

# create a new 'Resample To Image'
resampleToImage1 = ResampleToImage(registrationName='ResampleToImage1', Input=nc2)
resampleToImage1.UseInputBounds = 0
resampleToImage1.SamplingDimensions = [500, 500, 50]
resampleToImage1.SamplingBounds = [30.027099609375, 49.987098693847656, 10.027099609375, 29.98710060119629, -3178.0, -2.0]

# create a new 'XDMF Reader'
bathymetryxmf = XDMFReader(registrationName='bathymetry.xmf', FileNames=[path])
bathymetryxmf.PointArrayStatus = ['depth']
bathymetryxmf.GridStatus = ['Grid']

# create a new 'Warp By Scalar'
warpByScalar1 = WarpByScalar(registrationName='WarpByScalar1', Input=bathymetryxmf)
warpByScalar1.Scalars = ['POINTS', 'depth']
warpByScalar1.ScaleFactor = 0.00025

# create a new 'NetCDF Reader'
nc1 = NetCDFReader(registrationName='nc1', FileName=[path])
nc1.Dimensions = '(Z_MIT40, YG, XC)'
nc1.SphericalCoordinates = 0

# create a new 'Resample To Image'
resampleToImage3 = ResampleToImage(registrationName='ResampleToImage3', Input=nc1)
resampleToImage3.UseInputBounds = 0
resampleToImage3.SamplingDimensions = [500, 500, 50]
resampleToImage3.SamplingBounds = [30.027099609375, 49.987098693847656, 10.007100105285645, 29.967100143432617, -3178.0, -2.0]

# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(registrationName='AppendAttributes1', Input=[resampleToImage3, resampleToImage1, resampleToImage2])

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=appendAttributes1)
calculator1.ResultArrayName = 'UVW'
calculator1.Function = 'U*iHat + V*jHat + SALT*kHat'

# create a new 'Transform'
transform1 = Transform(registrationName='Transform1', Input=calculator1)
transform1.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform1.Transform.Scale = [1.0, 1.0, 0.00025]

# create a new 'Glyph'
glyph1 = Glyph(registrationName='Glyph1', Input=transform1,
    GlyphType='Arrow')
glyph1.OrientationArray = ['POINTS', 'UVW']
glyph1.ScaleArray = ['POINTS', 'UVW']
glyph1.ScaleFactor = 1.9960000038146974
glyph1.GlyphTransform = 'Transform2'
glyph1.GlyphMode = 'Uniform Spatial Distribution (Surface Sampling)'
glyph1.MaximumNumberOfSamplePoints = 100000
glyph1.Seed = 21322

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=warpByScalar1)
threshold1.Scalars = ['POINTS', 'depth']
threshold1.ThresholdRange = [-3073.121826171875, -1e-06]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from glyph1
glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'UVW'
uVWLUT = GetColorTransferFunction('UVW')
uVWLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.5431976343862054, 0.865003, 0.865003, 0.865003, 1.0863952687724108, 0.705882, 0.0156863, 0.14902]
uVWLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', 'UVW']
glyph1Display.LookupTable = uVWLUT
glyph1Display.SelectTCoordArray = 'None'
glyph1Display.SelectNormalArray = 'None'
glyph1Display.SelectTangentArray = 'None'
glyph1Display.OSPRayScaleArray = 'SALT'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'UVW'
glyph1Display.ScaleFactor = 2.017947769165039
glyph1Display.SelectScaleArray = 'None'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'None'
glyph1Display.GaussianRadius = 0.10089738845825195
glyph1Display.SetScaleArray = ['POINTS', 'SALT']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'SALT']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 40.65401896585767, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 40.65401896585767, 1.0, 0.5, 0.0]

# show data from threshold1
threshold1Display = Show(threshold1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold1Display.Representation = 'Feature Edges'
threshold1Display.AmbientColor = [0.49411764705882355, 0.49411764705882355, 0.49411764705882355]
threshold1Display.ColorArrayName = ['POINTS', '']
threshold1Display.DiffuseColor = [0.49411764705882355, 0.49411764705882355, 0.49411764705882355]
threshold1Display.SelectTCoordArray = 'None'
threshold1Display.SelectNormalArray = 'None'
threshold1Display.SelectTangentArray = 'None'
threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display.SelectOrientationVectors = 'None'
threshold1Display.ScaleFactor = -2.0000000000000002e+298
threshold1Display.SelectScaleArray = 'None'
threshold1Display.GlyphType = 'Arrow'
threshold1Display.GlyphTableIndexArray = 'None'
threshold1Display.GaussianRadius = -1e+297
threshold1Display.SetScaleArray = [None, '']
threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display.OpacityArray = [None, '']
threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display.PolarAxes = 'PolarAxesRepresentation'
threshold1Display.OpacityArrayName = [None, '']

# setup the color legend parameters for each legend in this view

# get color legend/bar for uVWLUT in view renderView1
uVWLUTColorBar = GetScalarBar(uVWLUT, renderView1)
uVWLUTColorBar.Title = 'UVW'
uVWLUTColorBar.ComponentTitle = 'Magnitude'

# set color bar visibility
uVWLUTColorBar.Visibility = 1

# show color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'UVW'
uVWPWF = GetOpacityTransferFunction('UVW')
uVWPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.0863952687724108, 1.0, 0.5, 0.0]
uVWPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(threshold1)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')
