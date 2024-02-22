export PYTHONPATH=$PYTHONPATH:$PWD
reset && python rigl/mnist/mnist_train_eval.py --mask_record_frequency=10 --save_path=/localdisk/Abhishek/rigl/ --training_method=rigl --file_name='runBand'
