function output = uploadToGoogle(dropboxAccessToken,varargin)
...
    dataFile = varargin{1};
...
% Read file contents
try
    fid = fopen(dataFile, 'r');
    data = char(fread(fid)');
    fclose(fid);
catch someException
    throw(addCause(MException('uploadToGoogle:unableToReadFile','Unable to read input file.'),someException));
end
% Generate the custom header
[~,remoteFName, remoteExt] = fileparts(dataFile);
headerFields = {'Authorization', ['Bearer ', dropboxAccessToken]};
headerFields{2,1} = 'Content-Type';
headerFields{2,2} = 'application/octet-stream';
headerFields = string(headerFields);
% Set the options for WEBWRITE
opt = weboptions;
opt.MediaType = 'application/octet-stream';
opt.CharacterEncoding = 'ISO-8859-1';
opt.RequestMethod = 'post';
opt.HeaderFields = headerFields;
% Upload the file
...
try
tempOutput = webwrite('https://www.googleapis.com/upload/drive/v3/files?uploadType=media', data, opt);

% update file name
mtdt = struct('Corrplot',[remoteFName remoteExt]);
headerFields{2,2} = 'application/json';
opt.HeaderFields = headerFields;
opt.RequestMethod = 'patch';
opt.MediaType = 'application/json';
webwrite(['https://www.googleapis.com/drive/v3/files/' tempOutput.id],mtdt, opt)
catch someException
end
...