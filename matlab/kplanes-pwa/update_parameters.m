function [C, d] = update_parameters(x, y, responsabilities)
% UPDATE_PARAMETERS -

  M=size(responsabilities,1);
  N=size(x,2);
  N_k=sum(responsabilities,2);
  theta=[x' ones(size(x',1),1)];
  for i=1:M
      Gamma=diag(sqrt(responsabilities(i,:)));
      pseudo=(Gamma*theta)'*(Gamma'*theta);
      temp=(Gamma*theta)'*(Gamma'*y');
      % temp=(pseudo\x)*Gamma;
      phi(:,i)=pseudo\temp;
      C(:,i)=phi(1,i);
      d(:,i)=phi(2,i);
  end
end
