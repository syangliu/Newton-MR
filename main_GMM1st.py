"""
Code for "Stability Analysis of Newton-MR Under Hessian Perturbations".
Authors: Yang Liu, Fred Roosta. ArXiv:1909.06224
Recover Figure 7. Performance profile for 500 runs of Newton-MR variants and 
several first-order methods
"""

from initialize import initialize

class learningRate():
    def __init__(self, value):
        self.value = value
        
class algPara():
    def __init__(self, value):
        self.value = value
        
#initialize methods
data = [
        ]

prob = [
        'gmm',
        ]

methods = [
        'Newton_MR',
        'Momentum',
        'Adagrad',
        'Adadelta',
        'RMSprop',
        'Adam',
        'SGD',
        ]

regType = [
        'None',
#        'Convex',
#        'Nonconvex',
        ] 

#initial point
x0Type = [
#        'randn',
#        'rand',
#        'ones'
        'zeros', # note: 0 is a saddle point for fraction problems
        ]

#initialize parameters
algPara.mainLoopMaxItrs = 1E5 #Set mainloop stops with Maximum Iterations
algPara.funcEvalMax = 300 #Set mainloop stops with Maximum Function Evaluations
algPara.innerSolverMaxItrs = 200 
algPara.lineSearchMaxItrs = 50
algPara.gradTol = 1e-10 #If norm(g)<gradTol, minFunc loop breaks
algPara.innerSolverTol = 0.01 #Inexactness of inner solver
algPara.beta = 1E-4 #Line search para
algPara.beta2 = 0.4 #Wolfe's condition for L-BFGS
algPara.show = False # print value in every iteration
#algPara.show = True # print value in every iteration
#for synthetic data GMM model

##### for gmm full gradient #### suggest algPara.funcEvalMax = 300
learningRate.Momentum = 3.780902679584121e-08
learningRate.Adagrad = 0.559579009451796
learningRate.Adadelta = 52.35649836867911
learningRate.RMSprop = 0.022237930017769372
learningRate.Adam = 0.06483601909442344
learningRate.SGD = 1.7142320415879017e-08
batchsize = 1 # full gradient

##### for gmm 0.05 #### suggest algPara.funcEvalMax = 17
#learningRate.Momentum = 1.559380940453686e-08
#learningRate.Adagrad = 0.33843733421550093
#learningRate.Adadelta = 60.16392553308128
#learningRate.RMSprop = 0.019312483380718334
#learningRate.Adam = 4.7983972608695656E-2
#learningRate.SGD = 1.9906519582939506e-08
#batchsize = 0.05 # proportion of mini-batch size

# comment off HProp if you don't want subsampling
HProp_all = [0.05] # \leq 3 inputs
fullHessian = False #Run full Hessian cases for all methods
# multiple run performance profile plot
total_run = 500
    
## Initialize
initialize(data, methods, prob, regType, x0Type, HProp_all, batchsize, 
           algPara, learningRate, total_run, fullHessian)









