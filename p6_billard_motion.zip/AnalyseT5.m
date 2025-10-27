Xr = [230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,230,225,221,213,210,206,203,195,192,189,185,179,175,172,168,162,158,155,151,145,142,139,136,129,128,131,131,136,137,139,140,144,145,147,149,151,153,155,156,159,161,163,164,167,168,170,172,175,176,178,179,182,183,184,186,189,190,191,193,195,196,198,199,201,202,203,205,207,209,209,211,213,213
];
Yr = [319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,319,315,312,306,303,301,297,291,290,287,285,280,277,274,271,267,264,261,259,255,252,249,247,242,239,239,237,233,231,229,229,225,223,222,221,217,216,214,213,210,209,207,206,203,202,200,198,195,194,193,191,189,187,187,185,183,181,180,179,176,175,174,173,171,169,168,167,165,163,163,161,159,159
];
Xy = [243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,243,242,242,242,242,242,242,242,242,242,242
];
Yy = [344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344,344
];
Xw = [239,239,239,239,245,265,284,302,340,359,378,397,434,453,472,491,527,545,563,580,616,635,652,670,705,723,720,705,676,663,651,641,621,612,603,595,578,569,560,552,535,526,518,509,492,484,476,467,451,442,434,426,409,401,393,385,368,360,352,344,328,320,312,304,288,280,272,264,248,241,237,234,227,223,219,215,208,204,200,197,189,186,182,178,171,167,164,160,153,149,146,143,136,132,129,128,133,135,137,138,142,144,146,147,151,152,154,156,159,161,162,164,167,168,169,171,173,175,176,178,180,181,182,184,186,187,188,190,192,193,194,195,197,198,199,200,202,203,204,205,207,208
];
Yw = [368,368,368,368,369,370,372,373,377,380,382,383,387,389,391,392,391,390,389,387,386,385,384,383,381,380,382,385,390,392,391,389,386,384,383,382,379,378,376,375,373,371,370,369,367,365,364,362,360,359,357,356,354,352,351,350,347,346,345,343,341,339,338,337,335,333,332,331,328,327,329,332,336,337,339,341,344,346,348,350,353,355,356,358,361,363,365,366,369,371,373,374,378,379,381,382,383,383,384,385,386,387,388,388,390,390,391,391,392,393,393,393,393,393,393,392,391,391,391,390,390,390,389,389,388,388,388,387,387,386,386,386,386,385,385,385,384,384,384,383,383,383
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
a = sprintf("Scores sheet - T5 – (%s)", date);
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

saveas(gcf,'ScoreSheetT5.pdf','pdf')

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

