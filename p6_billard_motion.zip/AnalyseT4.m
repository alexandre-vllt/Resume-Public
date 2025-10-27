Xr = [685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685,685
];
Yr = [237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237
];
Xy = [180,180,180,180,177,171,157,151,144,138,127,127,129,133,142,146,150,154,161,164,168,171,178,182,185,189,196,199,202,206,212,216,219,222,229,232,235,238,245,248,251,253,256,257,259,260,263,264,257,248,232,224,218,212,200,193,187,181,169,163,157,151,139,133,127,128,137,140,143,146,152,155,158,161,167,170,173,176,182,185,187,190,196,199,202,205,210,213,216,219,224,227,230,232,236,238,240,243,247,249,251,253,258,259,261,263,267,269,271,273,278,280,283,284,288,290,292,293,297,299,301,302,306,308,310,312,315,317,319
];
Yy = [299,299,299,299,294,272,231,210,191,173,137,120,105,103,126,137,147,156,173,182,190,198,215,223,231,240,255,263,272,280,296,304,312,320,336,344,352,360,375,383,391,389,378,373,369,365,356,352,346,339,328,322,316,310,299,293,287,282,271,265,259,254,243,237,231,227,220,216,212,208,200,196,192,188,181,177,173,169,161,158,154,150,143,139,135,132,124,121,117,113,106,103,100,102,107,109,111,113,117,119,120,122,126,128,130,132,136,138,139,142,145,147,149,151,155,156,158,159,163,165,167,168,171,173,175,177,180,182,183
];
Xw = [131,131,148,170,194,223,281,309,338,365,422,449,476,504,558,585,609,631,675,697,719,718,680,662,644,627,595,580,565,551,524,512,500,487,463,451,439,426,402,390,378,367,345,335,324,313,291,281,279,279,277,275,273,271,266,263,261,259,254,252,250,247,243,241,239,236,232,230,228,225,221,219,217,215,211,208,206,204,200,198,196,194,190,188,186,184,180,178,176,174,171,169,167,165,161,160,158,156,152,151,149,147,144,142,140,139,135,133,132,130,127,128,129,130,131,132,133,133,135,136,136,137,138,139,140,140,141,142,143
];
Yw = [391,391,368,335,310,299,274,261,247,233,203,187,171,154,121,104,108,122,148,160,172,183,204,214,224,234,253,261,270,279,295,303,311,318,334,342,349,357,372,380,387,391,382,377,373,369,360,356,354,353,349,347,345,342,338,336,334,332,327,325,323,321,317,315,313,311,307,305,303,301,297,295,293,291,287,286,284,282,278,276,274,272,269,267,266,264,260,259,257,255,252,250,248,247,243,241,240,238,235,234,232,230,227,226,224,223,220,218,217,216,213,211,209,207,203,201,199,197,194,192,190,188,184,183,181,179,176,174,173
];

Yr = 480-Yr;
Yy = 480-Yy;
Yw = 480-Yw;

[Xmin, Xmax,Ymin,Ymax] = GetFrame(Xr,Yr,Xy,Yy,Xw,Yw);

[Xr, Yr] = RemoveOutlier(Xr,Yr);
[Xy, Yy] = RemoveOutlier(Xy,Yy);
[Xw, Yw] = RemoveOutlier(Xw,Yw);

% on verifie le cas : si il manque des balles sur toutes la sequences cad qu'il a une tableau de cpoordonnées composé uniquement de NaN, alors on transforme le tableau en tableau de 0 et nous n'appelons pas interpolate Nan.
if isnan(Xr)
    Xr = 0*ones(1,length(Xr));
    Yr = 0*ones(1,length(Yr));
elseif isnan(Yr)
    Yr = 0*ones(1,length(Yr));
    Xr = 0*ones(1,length(Xr));
else
    [Xr, Yr] = InterpolateNan(Xr,Yr);
end

if isnan(Xy)
    Xy = 0*ones(1,length(Xy));
    Yy = 0*ones(1,length(Yy));
elseif isnan(Yy)
    Yy = 0*ones(1,length(Yy));
    Xy = 0*ones(1,length(Xy));
else
    [Xy, Yy] = InterpolateNan(Xy,Yy);
end

if isnan(Xw)
    Xw = 0*ones(1,length(Xw));
    Yw = 0*ones(1,length(Yw));
elseif isnan(Yw)
    Yw = 0*ones(1,length(Yw));
    Xw = 0*ones(1,length(Xw));
else
    [Xw, Yw] = InterpolateNan(Xw,Yw);
end

Ly = GetBallPathLength(Xy, Yy);
Lr = GetBallPathLength(Xr, Yr);
Lw = GetBallPathLength(Xw, Yw);

MoveDistPx = 9;
[idx, MoveDist] = GetFirstMoveIdx(Xr,Yr, MoveDistPx);

[FirstBall,SecondBall,LastBall, NbBallsMoved] = GetBallMoveOrder(Xr, Yr, Xy, Yy, Xw, Yw, MoveDistPx);

BallBorderDist = 9;
% utilise des conditions pour pas imprimer les coordonnées si la boule n'est pas la donc que sa coordonnées en X soit egale a 0
hold on
if Xr(1) ~= 0 
    plot(Xr(1), Yr(1), "k-hexagram","MarkerEdgeColor","r", 'MarkerSize',15)
    plot(Xr, Yr, "r:*")
end
if Xy(1) ~= 0 
    plot(Xy(1), Yy(1), "k-hexagram","MarkerEdgeColor",[0.9290 0.6940 0.1250], 'MarkerSize',15)
    plot(Xy, Yy,":*", "MarkerEdgeColor", [0.9290 0.6940 0.1250])
end
if Xw(1) ~= 0 
    plot(Xw(1), Yw(1), "k-hexagram","MarkerEdgeColor","b", 'MarkerSize',15)
    plot(Xw, Yw, "b:*")
end


rectangle('position', [Xmin, Ymin, Xmax - Xmin, Ymax - Ymin]);


date = string(datetime);
a = sprintf("Scores sheet - T4 – (%s)", date);
title(a)


ind1r = GetFirstMoveIdx(Xr,Yr, MoveDistPx);
ind1w = GetFirstMoveIdx(Xw,Yw, MoveDistPx);
ind1y = GetFirstMoveIdx(Xy,Yy, MoveDistPx);

if FirstBall == 1 
    IdxTouch = GetTouchIdx(Xr,Yr,Xmin, Xmax, Ymin, Ymax, BallBorderDist);
    Ball = 'red';
    nbrebond = length(find(max(ind1w,ind1y) >= IdxTouch & IdxTouch >= min(ind1y, ind1w)));
end
if FirstBall == 2 
    IdxTouch = GetTouchIdx(Xy,Yy,Xmin, Xmax, Ymin, Ymax, BallBorderDist);
    Ball = 'yellow';
    nbrebond = length(find(max(ind1w,ind1r) >= IdxTouch & IdxTouch >= min(ind1r, ind1w)));
end
if FirstBall == 3
    IdxTouch = GetTouchIdx(Xw,Yw,Xmin, Xmax, Ymin, Ymax, BallBorderDist);
    Ball = 'white';
    nbrebond = length(find(max(ind1r,ind1y) >= IdxTouch & IdxTouch >= min(ind1y, ind1r)));
end
bandtouched = length(IdxTouch);

distr = GetBallPathLength(Xr,Yr);
distw = GetBallPathLength(Xw,Yw);
disty = GetBallPathLength(Xy,Yy);

color_win = [0.392157 1.000000 0.000000];
color_loose = [1.000000 0.000000 0.000000];
%% resulat de la partie 
if nbrebond >= 3 && NbBallsMoved == 3 
    result = 'Win';

    if FirstBall == 1  
        plot(Xr(IdxTouch(max(ind1w,ind1y) >= IdxTouch & IdxTouch >= min(ind1y, ind1w))), Yr(IdxTouch(max(ind1w,ind1y) >= IdxTouch & IdxTouch >= min(ind1y, ind1w))), "o","MarkerEdgeColor",color_win, 'MarkerSize', 15, 'Linewidth', 2)
    end
    if FirstBall == 2  
        plot(Xy(IdxTouch(max(ind1w,ind1r) >= IdxTouch & IdxTouch >= min(ind1r, ind1w))), Yy(IdxTouch(max(ind1w,ind1r) >= IdxTouch & IdxTouch >= min(ind1r, ind1w))), "o","MarkerEdgeColor",color_win, 'MarkerSize', 15, 'Linewidth', 2)
    end
    if FirstBall == 3
        plot(Xw(IdxTouch(max(ind1r,ind1y) >= IdxTouch & IdxTouch >= min(ind1y, ind1r))), Yw(IdxTouch(max(ind1r,ind1y) >= IdxTouch & IdxTouch >= min(ind1y, ind1r))), "o","MarkerEdgeColor",color_win, 'MarkerSize', 15, 'Linewidth', 2)
    end

else 
    result = 'Loose';

    if FirstBall == 1  
        plot(Xr(IdxTouch), Yr(IdxTouch), "o","MarkerEdgeColor",color_loose, 'MarkerSize', 15,  'Linewidth', 2)
    end
    if FirstBall == 2  
        plot(Xy(IdxTouch), Yy(IdxTouch), "o","MarkerEdgeColor",color_loose, 'MarkerSize', 15,  'Linewidth', 2)
    end
    if FirstBall == 3
        plot(Xw(IdxTouch), Yw(IdxTouch), "o","MarkerEdgeColor",color_loose, 'MarkerSize', 15,  'Linewidth', 2)
    end
end

%legende 
% legend('hahahahha', 'location' , 'southeastoutside')
text(Xmin+20 , Ymin-10, sprintf('Score sheet for "%s"', Ball))
text(Xmin+20 , Ymin-20, sprintf('---"%s"---', result))
text(Xmin+420 , Ymin-20, sprintf('%d band(s) touched', bandtouched))
text(Xmin+420 , Ymin-10, sprintf('%d ball(s) moved', NbBallsMoved))
text(Xmin+20 , Ymin-30, sprintf('red : %.0fpx', round(distr)))
text(Xmin+220 , Ymin-30, sprintf('yellow : %.0f px', round(disty)))
text(Xmin+420 , Ymin-30, sprintf('white : %.0f px', round(distw)))

 
axis off

saveas(gcf,'ScoreSheetT4.pdf','pdf')

hold off
% fonction qui calcule la distance parcouru par une balle 
% En utilisant pythagore (operation sur des vecteurs) on determine la distance entre deux coordonnées à l'aide de la fonction diff(X)  succésive puis on additionne ces longueurs grasse a la fct sum.
 
function PathLength = GetBallPathLength(X,Y)

length_vector = sqrt(diff(X).^2 + diff(Y).^2);
PathLength = sum(length_vector);

end

% fonction qui trouve les bords du billard
% On cherche les coordonnées maximales et minimales des balles pour
% determiner les bords du billard

function [Xmin, Xmax,Ymin,Ymax] = GetFrame(Xr,Yr,Xy,Yy,Xw,Yw)

Xmax = max([max(Xr) max(Xy) max(Xw)]);
Xmin = min([min(Xr) min(Xy) min(Xw)]);
Ymax = max([max(Yr) max(Yy) max(Yw)]);
Ymin = min([min(Yr) min(Yy) min(Yw)]);

end

%fonction qui determine si une boule a bougé pendant la partie et si oui à quel indice.
% On regarde si la distance entre sa première coordonnées et les autres est supérieurs à MoveDistPx ( condition si elle a bougé ). Si la boule a bougé on note l'indice de son premier mouvement dans FirstMoveIdx et la distance dans MoveDist.
% En revanche si elle n'a pas bougé on met FirstMoveIdx au dernier indice + 1. de maniere a ce que cet indice corresponde a un indice impossible. MoveDist sera alors definit a 0.
% De plus nous avons etudiez le cas a savoir si il manque une boule et donc que les opérations sur les vecteurs ne sont pas possibles.
function [FirstMoveIdx, MoveDist] = GetFirstMoveIdx(X,Y, MoveDistPx)
X1 = X(1);
Y1 = Y(1);
X = X - X1;
Y = Y - Y1;

if X1 == 0 && Y1 == 0
    d = 0;
else
    d = sqrt( X.^2 + Y.^2 );
end
if d <= MoveDistPx 
    FirstMoveIdx = length(X)+1;
    MoveDist = 0;
else
    FirstMoveIdx = find(d>MoveDistPx, 1);
    MoveDist = sqrt(X(FirstMoveIdx).^2 + Y(FirstMoveIdx).^2);
end

end

% cette fonction permet de récupérer tout les indices coorespondant a un rebond bord-boules.
% on s'épare les cas pour chaque bords de maniere a ce que si une boule touche deux bords d'affiler, sela est compter comme deux rebonds
% on cherche a lors les indices de X Y t.q la distance considerer entre les bords (calculer dans getFrame) et la boule soit inferieur ou egale a BallBorderDist.

function [IdxTouch]=GetTouchIdx(X,Y,Xmin, Xmax, Ymin, Ymax, BallBorderDist)

IdxTouch_Xmax = find( (X+BallBorderDist) >= Xmax);
b = [0, diff(IdxTouch_Xmax)];
IdxTouch_Xmax = IdxTouch_Xmax((b ~= 1).*IdxTouch_Xmax > 1);

IdxTouch_Xmin = find( (X-BallBorderDist) <= Xmin);
b = [0, diff(IdxTouch_Xmin)];
IdxTouch_Xmin = IdxTouch_Xmin((b ~= 1).*IdxTouch_Xmin > 1);

IdxTouch_Ymax = find( (Y+BallBorderDist) >= Ymax);
b = [0, diff(IdxTouch_Ymax)];
IdxTouch_Ymax = IdxTouch_Ymax((b ~= 1).*IdxTouch_Ymax > 1);

IdxTouch_Ymin = find( (Y-BallBorderDist) <= Ymin);
b = [0, diff(IdxTouch_Ymin)];
IdxTouch_Ymin = IdxTouch_Ymin((b ~= 1).*IdxTouch_Ymin > 1);

IdxTouch = sort([IdxTouch_Xmax, IdxTouch_Xmin, IdxTouch_Ymax, IdxTouch_Ymin]);

end

% fonction qui classe les boules dans l'odre de leur premier mouvement et qui renvoi aussi le nombres de boules qui ont bougé pendant la partie
% On commence par verifier si la boule a bouger et donc su FirstMoveIdx vaut la longueur du vecteur + 1 comme definit dans GetFirstMoveIdx
% nous cherchons donc ensuite a evaluer tout les cas possibles en commencant par chercher la plus petite de FirstMoveIdx et donc de l'appeler Firstball 
% Nous analysons ensuite la longueur de ce vecteur pour que si elle vaut 2 ou trois on comare les MoveDistPx et donc de savoir laquelle est la vrai premiere. 
% une fois que la firstball est definit, on fait de meme mais avec la plus grande Valeur de FirstMoveIdx pour definir la troisieme boules et on prossede a la meme methode que pour firstball. 
% enfin lorsque nous avons first et lastball, la deuxieme est celle qui manque et que l'on peut trouver avec la fct setdiff qui compore [lastball first ball] avec [1 2 3]

function [FirstBall,SecondBall,LastBall, NbBallsMoved] = GetBallMoveOrder(Xr, Yr, Xy, Yy, Xw, Yw, MoveDistPx) 

a = 3;

[FirstMoveIdxr, MoveDistr] = GetFirstMoveIdx(Xr,Yr, MoveDistPx);
if FirstMoveIdxr == length(Xr)+1
    a = a-1;
end
[FirstMoveIdxy, MoveDisty] = GetFirstMoveIdx(Xy,Yy, MoveDistPx);
if FirstMoveIdxy == length(Xy)+1
    a = a-1;
end
[FirstMoveIdxw, MoveDistw] = GetFirstMoveIdx(Xw,Yw, MoveDistPx);
if FirstMoveIdxw == length(Xw)+1
    a = a-1;
end

NbBallsMoved = a;

FirstMoveIdx = [FirstMoveIdxr, FirstMoveIdxy, FirstMoveIdxw];
MoveDist = [MoveDistr, MoveDisty, MoveDistw];

FirstBall = find(FirstMoveIdx == min(FirstMoveIdx));

if length(FirstBall) == 1
    LastBall = find(FirstMoveIdx == max(FirstMoveIdx));
    if length(LastBall) == 2
        LastBall = find(MoveDist == min(MoveDist(LastBall(1)), MoveDist(LastBall(2))));
    end 
end 

if length(FirstBall) == 2
    FirstBall = find(MoveDist == max(MoveDist(FirstBall(1)), MoveDist(FirstBall(2))));
    LastBall = find(FirstMoveIdx == max(FirstMoveIdx));
end

if length(FirstBall) == 3
    FirstBall = find(MoveDist == max(MoveDist));
    LastBall = find(MoveDist == min(MoveDist));
end

SecondBall = setdiff([1 2 3], [FirstBall LastBall]);

end

% fonction qui change les valeurs Nan en la prochaines valeur valide.
% Pour cela on utilise la fonction interp1.
% On fait attention au cas ou la première valeur est un Nan car il n'est pas traité par interp1.

function [X,Y]=InterpolateNan(X,Y)

ll = find(~isnan(X));
kk = find(~isnan(Y));
nn = find(isnan(X));
mm = find(isnan(Y));

nX = interp1([0 ll],X([1 ll]),nn,'next');
nY = interp1([0 kk],Y([1 kk]),mm,'next');

X(nn) = nX;
Y(mm) = nY;

if isnan(X(1))
    X(1)= X(2);
end
if isnan(Y(1))
    Y(1)= Y(2);
end

end

% fonction qui remplace les valeurs abérrantes par la valeur précendente.
% Pour cela on utilise la fonction isoutlier avec la méthode movmedian.
% Nous avons bien verifier que le outlier est bien en X et en Y.

function [X,Y]=RemoveOutlier(X,Y)

ix = find(isoutlier(X,'movmedian',10));
iy = find(isoutlier(Y,'movmedian',10));

idx = intersect(ix, iy);

if (isempty(idx) ~=1)

    if (idx(1) == 1)
        idx=idx(2:end);
    end

    X(idx)=X(idx-1);
    Y(idx)=Y(idx-1);
end

end 

