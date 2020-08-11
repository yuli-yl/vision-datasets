Steps:
1. Download Dataset: https://tiny-imagenet.herokuapp.com/
2. Unzip tiny-imagenet--200
3. run train_preprocessing.py and val_preprocessing.py
4. run calc_mean_std.py to get the mean and std
5. Load dataset with pytorch dataloaders:         
        train_data = dset.ImageFolder(train_dir, transform=train_transform)
        test_data = dset.ImageFolder(test_dir, transform=test_transform)
        
