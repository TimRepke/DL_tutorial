# Deep Learning Tutorial


# Setup
## Install dependencies
We are not looking for high performance GPU accelerated computations here, so a basic installation of [TensorFlow](https://www.tensorflow.org/) is sufficient. It is assumed, that you have Python3 installed on your computer. We recommend using a virtual environment, but that's up to you.

```
# go to your workspace (or whereever)
cd ~/your/workspace

# optional
virtualenv -p python3 venv # if missing: sudo pip install virtualenv
source venv/bin/activate

# install dependencies
pip install keras tensorflow jupyter numpy pandas
```

## Presenting the tutorial
Check out [RISE](https://github.com/damianavila/RISE), it's nice.
```
pip install RISE
jupyter-nbextension install rise --py --sys-prefix
jupyter-nbextension enable rise --py --sys-prefix
```

In case you broke your notebook, go to `Edit->Edit Notebook Metadata` and add
```
"livereveal": {
	"theme": "serif",
	"transition": "zoom",
	"width": 1100,
	"height": 900,
	"scroll": true
}
```
