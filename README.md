# Deep Learning Tutorial
This tutorial provides a brief introduction into the application of Artificial Neural Networks for classification tasks. We show 


## Setup
### Install dependencies
We are not looking for high performance GPU accelerated computations here, so a basic installation of [TensorFlow](https://www.tensorflow.org/) is sufficient. It is assumed, that you have Python3 installed on your computer. We recommend using a virtual environment, but that's up to you.

```bash
# go to your workspace (or whereever)
cd ~/your/workspace

# (optional)
virtualenv -p python3 venv # if missing: 'sudo pip install virtualenv'

# install dependencies
pip install keras tensorflow jupyter numpy pandas
```

### Before the tutorial
Since we might not have perfect internet connection during the hands on tutorial, please run 
```bash
cd ~/your/workspace

# (if using a virtual env)
source venv/bin/activate

# loading datasets and testing setup
python init.py

# (leave the environment again)
deactivate
```


### During the tutorial
Download the `DLTutorial.ipynb` file (or clone the repository) and store it in `~/your/workspace`.
```bash
cd ~/your/workspace

# (if using a virtual env)
source venv/bin/activate # 'deactivate' to leave the environment again

# start notebook server
jupyter-notebook .
```
A browser tab should open. In the list you should see the file we just downloaded - open it! If you never used jupyter before, consult [their introduction](http://jupyter-notebook.readthedocs.io/en/latest/notebook.html#notebook-user-interface).

### Presenting the tutorial
Check out [RISE](https://github.com/damianavila/RISE), it's nice.
```bash
pip install RISE
jupyter-nbextension install rise --py --sys-prefix
jupyter-nbextension enable rise --py --sys-prefix
```

In case you broke your notebook, go to `Edit->Edit Notebook Metadata` and add
```json
"livereveal": {
	"theme": "simple",
	"transition": "slide",
	"width": 1500,
	"height": 900,
	"scroll": false,
	"progress": true,
	"start_slideshow_at": 'beginning'
}
```
Alternative options:
- `transition`: none, fade, slide, convex, concave, zoom, linear
- `theme`: black, white, league, sky, beige, simple, serif, blood, night, moon, solarized
- `start_slideshow_at`: beginning, selected
To configure which cells are part of the presentation, activate `View->Cell Toolbar->Slideshow`. Nothing selected is part of the previous slide, 'slide' begins a new slide or 'sub-slide', 'fragment's are for step by step reveals on a slide, 'skip' is not shown during presentation, whereas 'notes' are there as your speaker notes (not working).

