# MatLab Scripts
This README file outlines the use of the .m scripts within this folder, and which packages need to be downloaded to run them. For  instructions on how to create the circuits used please refer to FILENAME

### Toolboxes and APIs
Please download the `Econometrics Toolbox` in order for the correlation plot to run. Also, please create a Zapier account to update the .png file.

## Main Function
These functions are the main matlab scripts and are used to download, process and update the drive files for use on the web application.

`SIOT_Analysis.m`: This is the main .m file used and is the only one used at this stage. It downloads the data from the google sheet file `Days_Combined`, processes it and creates a correlation plot. This plot is emailed to a gmail address. Zapier takes the attachment and saves it to the drive, overwriting the old .png file. The web application then embeds the file with the data.

`UploadToGoogle.m`: A file using a more traditional API to directly upload the .png file. Not used since it changed the web address and therefore the web address did not work.
