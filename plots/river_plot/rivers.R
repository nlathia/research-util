library(riverplot)

# Assume: nodes labelled with letters of alphabet

# Example data: nodes.csv
# ID,x,labels
# A,1,Cluster 0
# B,1,Cluster 1
# C,2,Cluster 0
# D,2,Cluster 1

# Example data: edges.csv
# N1,N2,Value
# A,C,0.3476
# A,D,0.652
# B,C,0.826
# B,D,0.176

ns = list(
        A=list(col="#00990099", srt=0),
        B=list(col="#FF000099", srt=0),
        C=list(col="#00006699", srt=0),
        D=list(col="yellow", srt=0),
        E=list(col="#F0F8FF", srt=0),
        F=list(col="#7FFFD4", srt=0),
        G=list(col="#8A2BE2", srt=0),
        H=list(col="#CD3333", srt=0),
        I=list(col="#8EE5EE", srt=0),
        J=list(col="#BCEE68", srt=0)
)

plot_file_name <- 'example_output/river.pdf'
nodes <- read.table('example_data/nodes.csv', sep=',', header=T)
edges <- read.table('example_data/edges.csv', sep=',', header=T)
pdf(plot_file_name)
plot(makeRiver(nodes, edges, node_styles=ns))
dev.off()

