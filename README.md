# ImageUpsampling
Image upsampling model.
This model upasmple 1080p images into 2160p. The model was trained on only single image. However, it provides substantial performance in different images. Thanks to the generalizable property of convolution.

<pre>
Model: "model"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 input (InputLayer)        [(None, 1080, 1920, 3)]   0         
                                                                 
 conv2d_transpose_1 (Conv2DT  (None, 2160, 3840, 8)    38408     
 ranspose)                                                       
                                                                 
 conv2d_transpose_2 (Conv2DT  (None, 2160, 3840, 16)   51216     
 ranspose)                                                       
                                                                 
 conv2d_transpose_3 (Conv2DT  (None, 2160, 3840, 16)   25616     
 ranspose)                                                       
                                                                 
 conv2d_transpose_4 (Conv2DT  (None, 2160, 3840, 3)    1203      
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
This Image is the only image that model was trained on:
![Image Comparision](https://github.com/NeuralDreamResearch/ImageUpsampling/blob/main/Screenshot%20from%202023-07-13%2020-53-25.png?raw=true)
This image is completely unseen:
![Unseen](https://github.com/NeuralDreamResearch/ImageUpsampling/blob/main/Screenshot%20from%202023-07-13%2021-02-56.png?raw=true)
