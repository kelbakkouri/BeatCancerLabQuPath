setImageType('FLUORESCENCE'); 

createFullImageAnnotation(true) 

runPlugin('qupath.imagej.detect.cells.WatershedCellDetection', '{"detectionImage":"Channel 1","requestedPixelSizeMicrons":0.5,"backgroundRadiusMicrons":8.0,"backgroundByReconstruction":true,"medianRadiusMicrons":0.0,"sigmaMicrons":1.5,"minAreaMicrons":10.0,"maxAreaMicrons":400.0,"threshold":300.0,"watershedPostProcess":false,"cellExpansionMicrons":5.0,"includeNuclei":false,"smoothBoundaries":true,"makeMeasurements":true}') 