# CS247-LightGCN-for-Netflix
This project is done for CS247-Advanced Data Mining CourseWork at UCLA. The LightGCN model is experimented on three existing datasets and we build an Adaptive LightGCN model to use on Gowalla, Amazon-Book and Yelp2018. Furthermore, the LightGCN and Adaptive Light GCN model was also tested on Netflix dataset. Netflix dataset available was an explicit feedback form which required pre-processing techniques as well.

# Download Netflix Dataset

## Run LightGCN on Baselines
1. Please download the Zip folder to your Google drive and unzip it. Parallely, it can also be cloned to local machine using the following command:
```bash
git clone https://github.com/fzbuzz/CS247-LightGCN-for-Netflix.git
```

2. The following notebook can be run directly from the Google colab after unzipping the folder to google drive:
```bash
##CS247-LightGCN-for-Netflix/LightGCN/New runLGCN.ipynb
```

3. In the .ipynb file, please change the location of CS247/LightGCN-PyTorch-master as present in the Google drive. 
Run every cell until above "!python main.py --decay=1e-4 --lr=0.001 --layer=4 --seed=2020 --dataset="netflix" --topks="[20]" --recdim=64 --model="mod_lgn" --epochs=1000"

4. Before running the cell, navigate to the folder "code" i.e.:
```bash
%cd code
/content/drive/Shareddrives/CS247/LightGCN-PyTorch-master/code
```
## Run LightGCN on Netflix Dataset

5. After navigating to the 'code' folder using a command line from the Google colab notebook, run the following command:
```bash
!python main.py --decay=1e-4 --lr=0.001 --layer=4 --seed=2020 --dataset="netflix" --topks="[20]" --recdim=64 
--model="mod_lgn" --epochs=1000
```

6. The above command can be changed for different datasets by modifying the arguments, epochs, etc. The --model parameter specifies if we are using the existing LGCN model or the modified version of LGCN model. While the existing one is "lgn", the modified one is "mod_lgn". Additionally, the --datasets can be modified to "gowalla", etc. if needed.

