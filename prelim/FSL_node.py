# coding: utf-8

# In[1]:

import nipype.interfaces.fsl as fsl
#importing in the nipype interface 
#import in the wrapper for nodes and workflows here

# In[ ]:

#create stand-alone node 
sample_bet = pe.Node(interface=fsl.BET(), name = 'bet')
sample_bet.inputs.in_file = 'file.nii.gz'
#try hardcoding with actual .nii from within directory 
sample_bet.inputs.frac = 0.7
#do I need an outfile here or will it automatically spit out in the same directory 
sample_bet.inputs.out_file = 'file.nii.gz'
#sample_bet.run() 
#not going to run from here bc this is node, not instance 


# In[ ]:

freeview -v file.nii.gz 

#if this initialization does not work, try the one below 
#file_bet.nii.gz:colormap=jet
#check results of the execution  

# In[ ]:

sample_fast = fsl.FAST()
#maybe this in_file shouldn't be defined if it's defined in the workflow connection?
sample_fast.inputs.in_files = results.outputs.out_file
#routing the BET output as FAST input 


# In[ ]:

#create a workflow 
workflow = pe.Workflow(name=preproc)
#preproc = preprocessing
workflow.base_dir = '.'


# In[ ]:

workflow.add_nodes([sample_bet, sample_fast])
#adds the nodes to the workflow


# In[ ]:

#connecting the nodes together 
workflow.connect(sample_bet, 'result.outputs.out_file', sample_fast, 'in files') 


# In[ ]:

#visualizing the workflow
workflow.write_graph() 

