taskset -c 0,1,2,3 python src/synthesize.py --lot_size 1500 --sgd_sigma 5 --sgd_epoch 40 --pca_sigma 10 --db mnist --alg p3gm --vaezsample --vaeloss --z_dim 20