function y = pwa(part,theta,x)
  y = (x<part(2)).*(theta(1,:)*[x' ones(size(x,2),1)]');
  for sidx=3:length(part)
    y = y + (x>=part(sidx-1)&x<part(sidx)).*([theta(sidx-1,:)]*[x' ones(size(x,2),1)]');
  end
end
