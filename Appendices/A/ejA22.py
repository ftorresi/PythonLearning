import sys
import numpy as np
import matplotlib.pyplot as plt

class GrowthLogistic:
    def __init__(self, show_plot_on_screen=False):
        self.experiments = []
        self.show_plot_on_screen = show_plot_on_screen
        self.remove_plot_files() #remove files from old runs
        
        
    def run_one(self, y0, q, N):
        """Run one experiment."""
        index=np.arange(N+1)
        y=np.zeros(N+1)
        y[0]=y0
        for i in index[1:]:
            y[i]=y[i-1]+q*y[i-1]*(1-y[i-1])
        
        plotfile = 'ejA22_y0_%4.2f_q_%3.1f_N_%d.png' % (y0, q, N)
        self.experiments.append({'y0': y0, 'q': q, 'N': N, 'y': y, 'plotfile': plotfile})
        
        plt.figure()
        tag='y0=%4.2f, q=%g' %(y0,q)
        plt.plot(index,y)
        plt.title(tag)
        plt.xlabel('Time Units')
        plt.ylabel('Normalized number of individuals')
        plt.savefig(plotfile)
        if self.show_plot_on_screen: plt.show()
        
    
    def run_many(self, y0_list, q_list, N):
        for q in q_list:
            for y0 in y0_list:
                self.run_one(y0, q, N)
                
                
    def remove_plot_files(self):
        """Remove plot files with names ejA22_y0_*.png."""
        import os, glob
        for plotfile in glob.glob('ejA22_y0_*.png'):
            os.remove(plotfile)
            
    
    def report(self, filename='ejA22_report.html'):
        """Generate an HTML report with plots of all
        experiments generated so far."""
        
        outfile=open(filename,"w")
        outfile.write("<html> \n")
        outfile.write("<body> \n")
        for e in self.experiments:
            outfile.write('<p><img src="%s">\n' % e['plotfile'])
        outfile.write("</html> \n")
        outfile.write("</body>")
        outfile.close()        






if __name__ == '__main__':
       
    N=50
    g = GrowthLogistic()
    g.run_many(y0_list=[0.01, 0.3], q_list=[0.1, 1, 1.5, 1.8] + [2, 2.5, 3], N=N)
    g.run_one(y0=0.01, q=3, N=1000)
    g.report()
