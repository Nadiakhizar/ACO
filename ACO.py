

import numpy as np
from scipy.stats import norm
import Functions
class ACO:
   
    def __init__(self):
       
        self.verbosity = True
        
        # Initial algorithm parameters
        self.max_iter = 100                             
        self.pop_size = 5                               
        self.s = 50
        self.t= 0.1
        self.xii = 0.85
        
        # Initial (NULL) problem definition
        self.num_var = 2                                
        self.var_ranges = [[0, 1],
                           [0, 1]]                      
        self.cost_function = None                       
        
        # Optimization results
        self.SA = None                                  
        self.best_solution = None                       
    # end def
            
            
    def variables(self, nvar, ranges):
        
        if len(ranges) != nvar:
            print'Error, number of variables and ranges does not match'
        else:
            self.num_var = nvar
            self.var_ranges = ranges
            self.SA = np.zeros((self.s, self.num_var))
    # end def
            
            
    def cost(self, costf):
        
        self.cost_function = costf
    # end def
    
    
    def parameters(self, maximam_iter, pop_size, s, t, xii):
       
        self.max_iter = maximam_iter
        self.pop_size = pop_size
        self.s = s
        self.t = t

        self.xii = xii
    # end def
    
    
    def verbosity(self, status):
       
        if type(status) is bool:
            self.verbosity = status
        else:
            print "Error received verbosity parameter is not boolean"

    # end def
    
    
    def _biased_selection(self, probabilities):
        
        r = np.random.uniform(0, sum(probabilities))
        for i, f in enumerate(probabilities):
            r -= f
            if r <= 0:
                return i
    # end def
         
         
    def optimize(self):
        
        if self.num_var == 0:
            print "Error, first set the number of variables and their boundaries"
        elif self.cost_function == None:
            print "Error, first define the cost function to be used"
        else:
            
            if self.verbosity:   print "Initialization to the achrive"
            # Initialize the archive by random sampling, respecting each variable's constraints
            pop = np.zeros((self.pop_size, self.num_var))
            w = np.zeros(self.s)
            
            for i in Xrange(self.s):
                for j in Xrange(self.num_var):
                    self.SA[i, j] = np.random.uniform(self.var_ranges[j][0], self.var_ranges[j][1])
                self.SA[i, -1] = self.cost_function(self.SA[i, 0:self.num_var])                            
            self.SA = self.SA[self.SA[:, -1].argsort()]                                                    
            
            x = np.linspace(1,self.s,self.s)
            w = norm.pdf(x,1,self.t*self.s)
            p = w/sum(w)                                                    
            
            if self.verbosity:   print "Algo for main loop"
            
            # Algorithm runs until it reaches maximum number of iterations
            for iteration in Xrange(self.maximam_iter):
                if self.verbosity:
                    print "[%d]" % iteration
                    print self.SA[0, :]
                
                Mi = self.SA[:, 0:self.num_var]                                                                     
                for ant in Xrange(self.pop_size):
                    l = self._biased_selection(p)
                    
                    for var in Xrange(self.num_var):
                        sigma_sum = 0
                        for i in Xrange(self.k):
                            sigma_sum += abs(self.SA[i, var] - self.SA[l, var])
                        sigma = self.xii * (sigma_sum/(self.s - 1))
                         
                        pop[ant, var] = np.random.normal(Mi[l, var], sigma)                                         
                        
                        # Deals with search space violation using the random position strategy
                        if pop[ant, var] < self.var_ranges[var][0] or pop[ant, var] > self.var_ranges[var][1]:                   
                            pop[ant, var] = np.random.uniform(self.var_ranges[var][0], self.var_ranges[var][1])
                            
                    pop[ant, -1] = self.cost_function(pop[ant, 0:self.num_var])                                     
                
                self.SA = np.append(self.SA, pop, axis = 0)                                                         
                self.SA = self.SA[self.SA[:, -1].argsort()]                                                         
                self.SA = self.SA[0:self.s, :]
            
            self.best_solution = self.SA[0, :]
            #sol=Functions.Sphere(self.best_solution)
            #print "cost"
            #print sol
            return self.best_solution  
    # end def
    
# end class 
