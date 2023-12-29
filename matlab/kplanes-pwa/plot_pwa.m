function plot_pwa(part,x,y,colors)
  scatter(x(x<part(2)),y(x<part(2)),10,colors{1})
  hold on
  for sidx=3:length(part)
    scatter(x(x>=part(sidx-1)&x<part(sidx)),y(x>=part(sidx-1)&x<part(sidx)),10,colors{sidx-1})
  end
  hold off
end
