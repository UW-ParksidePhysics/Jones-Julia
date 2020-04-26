%code written by Julia Jones and Michael Bencs

fileID = fopen('pythagorean_triples.txt', 'r');
of = fopen('pythagorean_triples_quadratic_roots.txt', 'wt');
formatSpec = '%d %d %d\n';
[A, count] = fscanf(fileID, formatSpec, [3 Inf]);

n=1;
while n <= count/3
    a = A(1, n);
    b = A(2, n);
    c = A(3, n);
    
    discr = b*b - 4*a*c;
    d= sqrt(discr);
    if a == 0
        disp('a cannot equal zero')
    end

    if discr < 0
        discr=-discr
        di = round((sqrt(discr)/(2*a)), 3);
        b2 = round(-b / (2*a), 3);
        fprintf(of, '%g %g %g', a, b, c); fprintf(of, '%g %s %g %s', b2, '+', di, 'i');fprintf(of, '%g %s %g %s\n', b2, '-', di,'i');

    elseif discr >= 0
        x1= round((-b-d)/(2*a));
        x2= round((-b+d)/(2*a));
        R = [x1, x2];
        fprintf(of, '%g %g %g', a, b, c); fprintf(of, '%g', R);fprintf(of, '\n');
    end
    n = n + 1;
   
end
type pythagorean_triples_quadratic_roots.txt
