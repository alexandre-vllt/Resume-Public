Xr = [267,267,266,255,251,241,235,227,223,215,211,203,199,192,188,184,183,181,179,177,175,173,174,169,168,165,165,163,161,159,157,155,153,151,149,147,145,143,143,140,139,137,137,135,135,134,134,132,131,131,130,129,128,127,127,129,129,129,130,129,130,131,131,131,131,133,133,134,134,135,135,136,136,136,136,137,137,138,138,139,139,139,140,141,140,141,141,142,143,143,143,143,144,144,144,145,145,146,146,146,147,147,147,147,147,147,147,147,147,148,149,149,149,149,149,149,150,150,150,151,151,151,151,151,151,151,151,151,151,152,152,152,152,152,152,152,153,153,152,153,153,153,153,153,154,153
];
Yr = [103,103,103,131,151,187,206,239,255,283,299,327,341,371,385,379,369,349,339,323,315,299,291,277,271,255,249,235,227,211,205,191,183,169,163,149,141,127,121,107,101,112,116,125,128,135,141,149,151,159,163,171,175,182,186,193,195,203,207,213,217,223,227,234,237,243,247,253,257,263,267,273,276,282,285,291,294,300,303,309,313,318,321,327,329,335,338,343,347,352,355,359,363,368,371,375,379,383,387,390,390,390,390,387,385,383,382,379,378,375,373,371,370,367,367,363,363,361,359,357,355,353,353,351,349,347,347,345,344,343,341,340,339,337,337,335,335,333,333,331,330,329,328,327,327,325
];
Xy = [712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,127,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,712,713,716,718,721,722,725,725,724,724,722,721,720,719,718,717,716,715,714,714,713,712,711,710,709,709,708,708,707,706,705
];
Yy = [313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,286,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,313,314,314,314,314,314,314,314,314,314,314,314,314,314,314,314,314,314,314,314,314,314,314,314,314,314,314,313,312,310,309,308,307,306,305,304,303,303,302,301,301,300,299,299,298,298,297,297,296,295,295,294,294,294,293,293,292
];
Xw = [251,251,267,316,342,394,419,469,493,539,563,609,632,678,701,713,694,657,639,606,590,560,546,520,508,485,473,451,439,417,405,383,371,348,337,314,302,279,268,245,234,211,200,177,166,144,132,139,148,164,171,183,189,201,207,219,225,237,243,254,260,272,278,289,295,307,312,324,330,341,347,358,364,375,380,392,397,408,413,424,430,441,446,457,462,473,478,489,494,505,510,520,526,536,541,551,556,566,572,581,587,597,602,612,616,626,631,641,646,655,660,670,675,684,689,698,702,707,710,716,718,724,725,725,723,720,719,716,715,711,709,705,703,699,697,694,692,688,686,683,681,677,675,672,670,667
];
Yw = [152,151,121,100,107,119,125,135,140,147,151,157,160,167,170,183,191,211,220,238,248,266,274,291,299,317,325,342,350,367,375,390,390,378,373,364,359,351,347,338,333,324,320,311,308,299,295,283,276,264,258,246,240,227,222,210,204,192,186,174,168,156,150,139,133,121,116,104,101,110,113,120,123,129,133,139,143,149,152,158,162,168,171,177,181,187,190,196,199,206,208,215,218,224,227,233,236,242,245,251,254,259,262,268,271,277,280,286,288,294,297,303,305,311,314,319,323,330,334,342,345,353,356,364,367,375,378,385,389,390,388,385,383,379,377,373,371,367,365,362,360,356,354,351,349,345
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
a = sprintf("Scores sheet - T9 – (%s)", date);
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

saveas(gcf,'ScoreSheetT9.pdf','pdf')

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

