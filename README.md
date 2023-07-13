# ImageUpsampling
Image upsampling model.
This model upsmple 1080p images into 2160p. The model was trained on only single image. However, it provides substantial performance

<pre>
Model: "model_1"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 input_2 (InputLayer)        [(None, 1080, 1920, 3)]   0         
                                                                 
 conv2d_transpose_4 (Conv2DT  (None, 2160, 3840, 8)    38408     
 ranspose)                                                       
                                                                 
 conv2d_transpose_5 (Conv2DT  (None, 2160, 3840, 16)   51216     
 ranspose)                                                       
                                                                 
 conv2d_transpose_6 (Conv2DT  (None, 2160, 3840, 16)   25616     
 ranspose)                                                       
                                                                 
 conv2d_transpose_7 (Conv2DT  (None, 2160, 3840, 3)    1203      
 ranspose)                                                       
                                                                 
 tf.math.multiply_1 (TFOpLam  (None, 2160, 3840, 3)    0         
 bda)                                                            
                                                                 
 tf.__operators__.add_1 (TFO  (None, 2160, 3840, 3)    0         
 pLambda)                                                        
                                                                 
=================================================================
Total params: 116,443
Trainable params: 116,443
Non-trainable params: 0
_________________________________________________________________
</pre>
