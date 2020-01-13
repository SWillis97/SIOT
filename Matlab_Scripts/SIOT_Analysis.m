clc
clear all

%Assign the ID of the sheet's web address for the csv api
Sheet_ID = '1HLoDasR_YAcyZkQLkCRk67cBzrFpOnLatv81vD_qb3A';

%Import the speadsheet of day averages as a .csv file
Day_Averages = GetGoogleSpreadsheet(Sheet_ID);

%Find how many days are currently being considered and remove headings 
%from the csv file.
Day_Nos = size(Day_Averages);
Day_length = Day_Nos(1) - 1;
Day_Averages = Day_Averages(2:Day_length+1,:);

double_lists = [];

figure(1)
for n = 1:Day_Nos(2)
% Plots the scaled data
    [double_lists,Current_List] = List_Sorter(double_lists,Day_Averages,n);
    plot_data =plot(Current_List);
    hold on
end

%title('Scaled Day Averages for Humidity, Temperature and Footsteps taken')
xlabel('Day Number') 
ylabel('Scaled  Total')
legend({'Humidity','Temperature','Footsteps'},'Location','southoutside','Orientation','horizontal')

% Create and save new plots for the web app
saveas(plot_data, 'plot.png')
double_lists = double_lists';
rho = corr(double_lists);
corrplot(double_lists)
saveas(gcf,'corrplot.png'); 
corrplot_file = imread('corrplot.png');

% Emails the new png file to a gmail account. This account is linked to the
% drive so that new files are saved
sendmail('samuelwil1997@gmail.com','test','here you are','corrplot.png')

function [double_matrix,Output_List] = List_Sorter(double_matrix,Day_Averages,n)
% Converts cells into doubles for plotting and then scales them
    Output_List = str2double(Day_Averages(:,n)');
    double_matrix = [double_matrix; Output_List];
    Output_List = Output_List - min(Output_List);
    Output_List = 100*(Output_List/max(Output_List));
end

function result = GetGoogleSpreadsheet(DOCID)
% This function imports the data from the google sheets file for processing
loginURL = 'https://www.google.com'; 
csvURL = ['https://docs.google.com/spreadsheet/ccc?key=' DOCID '&output=csv&pref=2'];

%go to google.com to collect some cookies
cookieManager = java.net.CookieManager([], java.net.CookiePolicy.ACCEPT_ALL);
java.net.CookieHandler.setDefault(cookieManager);
handler = sun.net.www.protocol.https.Handler;
connection = java.net.URL([],loginURL,handler).openConnection();
connection.getInputStream();

%go to the spreadsheet export url and download the csv
connection2 = java.net.URL([],csvURL,handler).openConnection();
result = connection2.getInputStream();
result = char(readstream(result));

%convert the csv to a cell array
result = parseCsv(result);

end

function data = parseCsv(data)
% splits data into individual lines
data = textscan(data,'%s','whitespace','\n');
data = data{1};
for ii=1:length(data)
   %for each line, split the string into its comma-delimited units
   %the '%q' format deals with the "quoting" convention appropriately.
   tmp = textscan(data{ii},'%q','delimiter',',');
   data(ii,1:length(tmp{1})) = tmp{1};
end

end

function out = readstream(inStream)
%READSTREAM Read all bytes from stream to uint8

import com.mathworks.mlwidgets.io.InterruptibleStreamCopier;
byteStream = java.io.ByteArrayOutputStream();
isc = InterruptibleStreamCopier.getInterruptibleStreamCopier();
isc.copyStream(inStream, byteStream);
inStream.close();
byteStream.close();
out = typecast(byteStream.toByteArray', 'uint8'); 

end


