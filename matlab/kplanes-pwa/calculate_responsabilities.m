function responsabilities = calculate_responsabilities(x, y, C, d)
% CALCULATE_RESPONSABILITIES -
  M=size(d,2);
  N=size(x,2);
  for i=1:M
    dist(:,i)=(y-(C(:,i)'*x+d(:,i))).^2;
    % likelihood=mvnpdf(y',(C(:,i)'*x+d(:,i))',Sigma(:,:,i));
    % respNum(:,i)=likelihood_mod;
  end
  responsabilities = ((1+dist)./(min(dist+1,[],2))==1)'*1;
end
