%this code was written and designed by Julia Jones and Michael Bencs
n=input('Largest "c" value: ')
of= fopen('pythagorean_triples.txt','wt');
   for a=1:1000
        for b=1:a
            for c=1:n-1
                if c == sqrt(a^2  + b^2)
                    
                    formatSpec = '%g  %g  %g \n';
                    fprintf(of, formatSpec, a, b, c)
                end
            end
        end
    end
fclose(of);

type pythagorean_triples.txt

 
    
  
