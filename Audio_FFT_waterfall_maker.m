% made by thegmr140  on youtube.com  

clear all
close all
h = 800;
w = 400;
[filename, pathname, filterindex] = uigetfile('*.*','Pick a Image file','c:\FFT_Image');
b = [pathname filename];
x = imread(b);

%
x = rgb2gray(x);
x = double(x);
x = x / max( x(:) );
x = x(end:-1:1,:);
x = imresize(x,[h w] );

pdata = 23 * randn(h,w);
pdata = exp(1i * pdata);

x = x .* pdata;

x1 = conj( x(:,end:-1:2) );
x = [x1 x];
x = ifftshift(x,2);
x = ifft(x,[],2);


x = reshape(x.',1,[] );
x = real(x);

x = x / max(x);

% plot(real(x))
% hold on
% plot(imag(x))
% hold off


audiowrite('c:\temp\AudioWaterfall.wav',x,24000,'BitsPerSample',16);






