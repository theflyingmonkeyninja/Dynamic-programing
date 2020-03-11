function hanoiTower(n,A,B,C)
if n >0
    hanoiTower(n-1,A,C,B);
    move(A,C);
    hanoiTower(n-1,B,A,C);

 
end
end

function move(A,B)
 disp (['move disk from ', A, ' to ',B]);
end
