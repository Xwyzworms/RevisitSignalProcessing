srate = 1000;
time = 0:1/srate:3;
n = length(time);
p = 15;

% Noise level, measured in standard deviation
noiseAmp = 5;

ampl = interp(rand(p,1)*30, linspace(l,p,n));
noise = noiseAmp * randn(size(time));
signal = ampl + noise;

%% initialize the running mean filter :
filtSig = zeros(size(signal));

k = 20;
for i=k+1:n-k-1
    filtSig(i) = mean(signal(i-k:i+k)) ;
end
%% Compute the windowsize
windowSize = 1000*(k*2+1) / srate;



