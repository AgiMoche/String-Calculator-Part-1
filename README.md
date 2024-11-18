Validate a South African ID number (625)
For raw project instructions see: http://syllabus.africacode.net/language-agnostic/validate-id-number/

## Project Setup

### 1. Environment Setup:
In the instructions below, information is provided to install the necessary tools needed to run the notebook and its dependencies on any capable machine:
- Use the following command in Windows Terminal or Command Prompt to create a virtual environment:
  1. Create a new virtual environment to run the tests in by using the following command in the terminal window: 
  ~~~
  python -m venv <virtual_environment_name>
  ~~~
  2. Activate the new virtual environment that you just created using the following command:
  ~~~
  <virtual_environment_name>\Scripts\activate
  ~~~
  
### 2. Cloning the Repository:
In the instructions below, information is provided to clone the repository of the project. Cloning the repository pulls down a full copy of all the repository data associated with the GitHub.com uploads:
- Use the following command in Windows Terminal or Command Prompt to clone the repository: 
~~~
git clone https://github.com/Umuzi-org/Oageng-Moche-625-validate-a-south-african-id-number-python.git
~~~
  
### 3. Installing the Required Python Packages:
Once the repository has been cloned and the virtual environment has been set up:
1. Navigate to the project directory by using the following command in the virtual environment Command Terminal or Windows Terminal:
~~~
cd Oageng-Moche-625-validate-a-south-african-id-number-python
~~~
- Once the virtual environment has been set up and activated, you will need to install all the relevant packages for the project
2. In the Windows Terminal or Command Prompt of the virtual environment, type in the following command to install the modules required to run the files for the project:
~~~
pip install -r requirements.txt
~~~
3. Ensure that Setuptools is installed on your machine. If you are unsure that Setuptools is installed on your machine, use the following command in the virtual environment Command Terminal or Windows Terminal to install it:
~~~
pip install setuptools
~~~
4. Once Setuptools has been installed on your machine, the packages will need to be installed in the newly activated virtual environment by running the following command in the Windows Terminal or Command Prompt:
~~~
python setup.py develop
~~~

### 4. Running the "Validate a South African ID number" project and its test cases:
- After installing the required packages, make sure you are in the project directory 
- If you are not in the project directory or unsure that you are in the project directory, navigate to the project directory by using the following command in the virtual environment Command Terminal or Windows Terminal: 
~~~
cd Oageng-Moche-625-validate-a-south-african-id-number-python
~~~
- To run the tests/test cases of the project, ensure that pytest is installed on your machine. If you are unsure that pytest is installed on your machine, use the following command in the virtual environment Command Terminal or Windows Terminal to install pytest:
~~~
pip install pytest
~~~
- Once pytest has been installed on your machine, to run the tests/test cases of the project, use the following command in the virtual environment Command Terminal or Windows Terminal:
~~~
python -m pytest
~~~

### 5. Deactivating environment setup:
Once the necessary tasks have been completed, deactivate the virtual environment that was set up to run the tasks by typing the following command in the Windows Terminal or Command Prompt:
~~~
deactivate
~~~
