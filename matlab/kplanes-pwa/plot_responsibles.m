function plot_responsibles(x, y, responsabilities, C, d, colors)
% PLOT_RESPONSIBLES -
  [~,z_hat]=max(responsabilities,[],1);
  M=size(d,2);
  N=size(x,2);
  t=min(x):max(x);
  hold on
  for i=1:M
      plot(t,C(:,i)'*t+d(:,i),'Color',colors{i})
  end

  for i=1:3
    z_i=find(z_hat==i);
    x_i=x(:,z_i);
    y_i=y(:,z_i);
    scatter(x_i(1,:),y_i(1,:),10,colors{i})
  end
  hold off
end
