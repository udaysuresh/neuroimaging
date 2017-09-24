clear all; close all;

%% visualization 
load([foldername{Ifolder} '/fit_results.mat'])

%% estimate bias field, normalized & remove
imute = imall(:,:,:,1); 
imute_plus = imallplus(:,:,:,1); 
brainmask_open = imdilate(brainmask, strel('disk', 16));
brainmask_open = permute(imdilate(permute(brainmask_open, [3 2 1]), strel('disk', 6)), [3 2 1]);
imbias = imgaussfilt3(abs(imute).*brainmask_open,6);
Snormall = max(abs(imute(I)));

imbias = imbias / Snormall;

switch Ifolder
    case 8
        sc_ut2 = [.055 .145]; sc_lt2 = [.2 1.4];
                 sc_ut2_t2 = [0 1.4]; sc_lt2_t2 = [30 55];
         sc_ut2_df = [-450 -200]; sc_lt2_df = [-100 100]; 
Iax = 37; Icor = 44; Isag = 48;
    Icrop = {[7:103], [1:imsize(2)], [1:83]};     Icor = Icor -6;

    
    case 3
         sc_ut2 = [.06 .16]; sc_lt2 = [.2 1.4]; 
         sc_ut2_t2 = [0 0.6]; sc_lt2_t2 = [10 40];
         sc_ut2_df = [-1200 -700]; sc_lt2_df = [-250 250]; 
         Iax = 36; Icor = 39; Isag = 49;
         Icrop = {[1:imsize(1)], [1:imsize(2)], [1:imsize(3)]};
end

         sc_AIC = [200 320];

%%
for Imaps = 3

clear dataplot
for Ix = 1:NI
    switch Imaps
        case 1
            dataplot(Ix) = fit_result2_plus(Ix,2).rho ./ imbias(I(Ix)); sc = sc_ut2; root_fname = 'uT2_corrected';
        case 3
     dataplot(Ix) = fit_result2_plus(Ix,2).T2; sc = sc_ut2_t2; root_fname = 'uT2_T2';
    end
                

end

datamask = (AIC2_plus < AIC_thresh(Ifolder));

alphamask = zeros(imsize);
alphamask(I) = datamask;

implot = zeros(imsize) - Inf;
implot(I) = dataplot .* datamask;

implot = implot(Icrop{1}, Icrop{2}, Icrop{3});
alphamask = alphamask(Icrop{1}, Icrop{2}, Icrop{3});

% figure(1)
% disp3d(implot,sc(1), sc(2), [Icor, Isag, Iax])

%% generate maps


h = figure;
subplot(131),sb1= imagesc(flipud((implot(:,:,Iax))), sc); axis off equal
set(sb1, 'AlphaData', squeeze(flipud((alphamask(:,:,Iax)))));
subplot(132), sb2= imagesc(squeeze((implot(:,Isag,:))).', sc); axis off equal
set(sb2, 'AlphaData', squeeze((alphamask(:,Isag,:))).');
subplot(133), sb3= imagesc(squeeze((implot(Icor,:,:))).', sc); axis off equal
set(sb3, 'AlphaData', squeeze(alphamask(Icor,:,:)).');
colormap(hot)
colorbar
set(gcf, 'color', [1 1 1]*.8)
% apply mask

if write_flag
print([foldername{Ifolder} '/' root_fname], '-dpdf')
end
end
