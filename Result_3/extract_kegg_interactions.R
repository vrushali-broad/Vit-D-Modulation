library(KEGGgraph)
library(KEGGREST)

packageVersion("KEGGgraph")
packageVersion("KEGGREST")

# Function to retrieve primary MGI gene symbols
getMGIGeneSymbols <- function(gene_ids) {
  gene_symbols <- sapply(gene_ids, function(id) {
    gene_symbol <- NA  # Default to NA if the gene symbol is not found
    tryCatch({
      gene_info <- keggGet(id)
      if (!is.null(gene_info[[1]]$SYMBOL)) {
        symbols <- strsplit(gene_info[[1]]$SYMBOL, ", ")[[1]]
        gene_symbol <- symbols[1]  # Assuming the first symbol is the primary MGI symbol
      }
    }, error = function(e) {
      message("Error retrieving info for ", id, ": ", e$message)
    })
    return(gene_symbol)
  }, USE.NAMES = TRUE)
  return(gene_symbols)
}

# Function to save unique nodes with MGI symbols to a file
saveKEGGPathwayNodesWithSymbols <- function(nodes, gene_symbols, filepath) {
  nodes_df <- data.frame(id = nodes, symbol = gene_symbols[nodes], stringsAsFactors = FALSE)
  unique_nodes_df <- unique(nodes_df)
  write.table(unique_nodes_df, file = filepath, quote = FALSE, row.names = FALSE, col.names = TRUE, sep = "\t")
}

# Function to save unique edges with MGI symbols to a file
saveKEGGPathwayEdgesWithSymbols <- function(edges, gene_symbols, filepath) {
  edges_df_list <- lapply(names(edges), function(x) {
    targets <- unlist(edges[[x]])
    if (length(targets) > 0) {
      source_symbol <- gene_symbols[x]
      target_symbols <- gene_symbols[targets]
      if (!is.na(source_symbol) && all(!is.na(target_symbols))) {
        return(data.frame(from = rep(source_symbol, length(target_symbols)), to = target_symbols, stringsAsFactors = FALSE))
      }
    }
    return(NULL)
  })
  edges_df <- do.call(rbind, edges_df_list)
  unique_edges_df <- unique(edges_df)
  write.table(unique_edges_df, file = filepath, quote = FALSE, row.names = FALSE, col.names = TRUE, sep = "\t")
}

# Function to process a KEGG pathway
processKEGGPathway <- function(pathway_id, organism = "mmu") {
  # Download and parse KGML file
  kgml_file <- getKGMLurl(pathway_id, organism = organism)
  download.file(kgml_file, destfile = paste0(pathway_id, ".xml"))
  pathway <- parseKGML2Graph(paste0(pathway_id, ".xml"))

  # Extract nodes and edges
  nodes <- nodes(pathway)
  edges <- edges(pathway)

  # Retrieve MGI gene symbols for nodes
  gene_symbols <- getMGIGeneSymbols(nodes)

  # Save nodes and edges with MGI symbols
  saveKEGGPathwayNodesWithSymbols(nodes, gene_symbols, paste0(pathway_id, "_nodes_with_mgi_symbols.txt"))
  saveKEGGPathwayEdgesWithSymbols(edges, gene_symbols, paste0(pathway_id, "_edges_with_mgi_symbols.txt"))
}

# Example usage for TCR and Calcium signaling pathways
processKEGGPathway("mmu04660")
processKEGGPathway("mmu04020")

