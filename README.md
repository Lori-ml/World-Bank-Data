# Click [here](https://myapp-worldbankdata-florida-1.herokuapp.com/) to view the webpage

Heroku changes policies on November 28 2022, hence above link does not work. 

![image](https://user-images.githubusercontent.com/41455899/210284159-213ce589-c37c-4dab-9d66-a2f16119862c.png)


## Project Description:

Goal of this project is to compare Finland, Denmark, Switzerland, Canada and USA in following areas: unemployment, employment in agriculture, inflation, and mortality caused by road traffic injury for timespan of 20 years (2000 – 2020). Data is extracted automatically through [World Bank Open Data indicators](https://data.worldbank.org/indicator/) APIs. 
 Following is a description of each chart.

**Chart 1:** Percentage of labor force that is without work but available for and seeking employment.

**Chart 2:** Percentage of women vs men employed in agriculture. Sector of agriculture consists in activities such as hunting, forestry and fishing.

**Chart 3:** Percentage of inflation as measured by consumer price index.

**Chart 4:** Mortality caused by road traffic injury per 100,000 population.
 
## How to install and run the project

Code in the workspace folder runs in [Ubuntu 22.04.1](https://apps.microsoft.com/store/detail/ubuntu-22041-lts/9PN20MSR04DW?hl=en-us&gl=us) LTS and [Anaconda for Linux](https://docs.anaconda.com/anaconda/install/linux/). Libraries needed to run the project locally are: Flask, Pandas, Plotly, Gunicorn, Requests, Matplotlib and Plotly.Express. For deploying the web app, create an account to [Heroku](https://signup.heroku.com/).
Below steps show how the project can be run locally. 

```python

# Update Python
conda update python

# Create a virtual environment
python3 -m venv worldbankvenv

# Activate the new environment (Mac/Linux)
source worldbankenv/bin/activate

#In addition to the existing Python packages in the new environment. Pip install following packages.

pip install flask pandas plotly gunicorn requests matplotlib plotly.express

#Install Heroku 

curl https://cli-assets.heroku.com/install-ubuntu.sh | sh

#Verify Heroku has been properly installed

heroku login -i

#Initialize git repository 

git init

#Configure email and username for git
git config --global user.email "you@example.com"
git config --global user.name "Your Name"

# Check which files that need to be committed

git add .
git status
git commit -m "example_message"

#Create a Heroku app

heroku create app_example_name

# Set environment variable to pass along with the push

heroku config:set SLUGIFY_USES_TEXT_UNIDECODE=yes
heroku config:set AIRFLOW_GPL_UNIDECODE=yes

# Verify the variables

heroku config

#Push changes to Heroku remote repo

git push heroku master

```

## Acknowledgements

Data for this project was extracted via API provided by [World Bank Open Data](https://data.worldbank.org/).
