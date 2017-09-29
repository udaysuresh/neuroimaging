%% really basic format for scrolling through image outputs, using to make brain slice GIFS

for e=1:32
imagesc(abs(imallplus(:,:,47,e)))
colormap(gray)
axis equal
pause
end

%% trying to make auto into gifs

h = figure;
axis tight manual % this ensures that getframe() returns a consistent size
filename = 'brain_slices.gif';
for e=1:32
    drawnow 
      % Capture the plot as an image 
      frame = getframe(abs(imallplus(:,:,47,e))); 
      im = frame2im(frame); 
      [imind,cm] = rgb2ind(im,256); 
      % Write to the GIF File 
      if n == 1 
          imwrite(imind,cm,filename,'gif', 'Loopcount',inf); 
      else 
          imwrite(imind,cm,filename,'gif','WriteMode','append'); 
      end 
  end