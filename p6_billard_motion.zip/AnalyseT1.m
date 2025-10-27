Xr = [667,667,667,651,619,559,531,499,471,419,400,379,361,323,304,287,267,235,219,203,187,154,137,129,143,168,181,192,203,224,233,243,252,271,279,287,297,314,323,331,341,357,367,375,383,401,410,419,426,443,451,461,469,487,495,503,511,529,537,545,555,571,579,587,595,611,619,628,635,648,655,661,667,679,685,691,699,711,718,723,725,715,712,709,705,699,696,692,689,683,679,677,674,668,665,661,659,653,650,646,644,639,635,633,629,624,621,618,616,610,607,604,601,596,594,591,588,583,580,577,576,570,568,565,563,558,555,552,550,545,543,540,538,533,532,529,527,522,519,517,515,511,508
];
Yr = [269,269,269,259,235,191,167,147,129,105,123,139,155,187,199,211,227,251,263,275,287,307,319,331,341,363,375,386,393,375,367,360,353,341,335,329,323,311,305,299,295,282,275,270,265,253,247,241,235,223,219,213,207,195,189,185,179,167,161,155,151,139,135,129,123,111,107,101,101,111,113,115,119,123,125,127,131,136,139,141,143,145,145,147,147,149,149,151,151,153,154,155,155,157,159,159,160,162,163,163,163,165,167,167,168,169,170,171,172,173,174,175,175,177,177,179,179,181,181,181,183,185,185,185,185,187,189,189,189,191,191,193,193,195,195,196,197,197,199,199,199,201,201
];
Xy = [718,NaN,NaN,682,692,712,721,723,716,704,698,691,682,664,656,647,637,620,612,604,596,579,571,562,554,537,529,520,513,496,488,480,471,455,447,440,435,424,419,414,409,398,392,387,381,370,365,360,355,344,339,334,328,318,313,307,302,292,287,282,277,267,262,256,252,241,236,231,227,217,212,207,202,192,187,182,178,168,163,158,154,145,140,135,131,128,131,134,137,141,143,146,148,153,158,159,157,159,160,161,162,163,164,165,166,168,168,169,170,170,171,172,172,174,174,175,176,177,178,178,179,180,181,181,182,183,184,184,185,186,186,187,187,188,188,189,190,190,191,191,192,193,193
];
Yy = [355,NaN,NaN,267,248,213,196,178,159,124,108,101,116,143,155,167,180,201,210,220,229,247,256,265,274,292,301,310,319,337,346,355,363,382,390,389,381,369,364,359,355,347,343,338,334,326,322,318,314,306,302,298,293,286,282,277,274,266,262,257,254,246,242,238,234,227,223,219,215,207,203,199,195,188,184,181,177,170,166,162,159,151,147,144,140,134,132,129,127,122,120,117,115,110,108,105,103,101,102,103,105,108,109,110,111,115,116,117,118,121,122,123,124,126,127,129,130,132,134,134,135,137,138,140,141,142,143,145,145,147,148,149,150,152,153,153,154,155,156,157,158,159,160
];
Xw = [169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,170,169,171,172,173,175,176,176,178,179,180,181,183,184,185,185,187,188,188,189,191,191,192,193,194,195,196,196,197,198,198,199,200,201,201,201,202,203,203,203,204,205,205,205,206,206,206,206,207,207
];
Yw = [113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,113,113,114,114,114,114,114,114,115,115,115,115,115,115,115,115,115,115,115,115,115,115,116,116,116,116,116,116,116,117,117,117,117,117,117,117,117,117,118,118,118,118,118,118,118,118,118
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
a = sprintf("Scores sheet - T1 – (%s)", date);
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

saveas(gcf,'ScoreSheetT1.pdf','pdf')

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

