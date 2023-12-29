clear; close all
%% Generate data

PI=pi;
emMaxIter=100;
N=200;
% N=5;
colorsgt={[ 0 0.447058823529412 0.741176470588235 ],[0.850980392156863   0.325490196078431   0.098039215686275],[0.929411764705882   0.694117647058824   0.125490196078431]};
colors={[ .5 0.447058823529412 0.741176470588235 ],[0.850980392156863   0.825490196078431   0.098039215686275],[0.929411764705882   0.694117647058824   0.625490196078431]};

m=[2 2.5 3];
n=[0 3 -2];
theta=[m; n]';
part=[-4 0 4 9];

M=length(part)-1;
f=@(C,d,x) C'*x+d;

x = part(1)+(part(end)-part(1))*rand(1,N);
x=sort(x);

y = pwa(part,theta,x);
figure(1)
plot_pwa(part,x,y,colors);

%% Initialize estimated parameters
indexpts1=randi([1 N-1],1,3);
C=(y(:,indexpts1+1)-y(:,indexpts1))./(x(:,indexpts1+1)-x(:,indexpts1));
d=y(:,indexpts1)-C.*x(:,indexpts1);
C=C+rand(1,M);
d=d+rand(1,M);
% C=m;
% d=n;

t=min(x):max(x);
hold on
for i=1:M
plot(t,f(C(:,i),d(:,i),t),'Color',colors{i})
end
hold off

responsabilities = calculate_responsabilities(x, y,C,d);
[C,d]=update_parameters(x, y, responsabilities);

plot_responsibles(x, y, responsabilities, C, d,colors)


for emInd=1:emMaxIter
    responsabilities=calculate_responsabilities(x,y,C,d);

    figure(1)
    subplot(2,1,2)
    cla
    plot_responsibles(x, y, responsabilities,C,d,colors);
    title("EM")

    [C,d]=update_parameters(x, y, responsabilities);
    [~,z_hat]=max(responsabilities,[],1);

  for i=1:3
    z_i=find(z_hat==i);
    clusterSize(i)=size(z_i,2);
  end

end
