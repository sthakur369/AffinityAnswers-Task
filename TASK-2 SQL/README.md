# SQL Questions

### Q1. How many types of tigers can be found in the taxonomy table of the dataset?
> *(HINT: use the biological name of the tiger)*

```
SELECT COUNT(ncbi_id)
FROM Rfam.taxonomy
WHERE species LIKE  "%tigris%";
```


### Q2. What is the "ncbi_id" of the Sumatran Tiger? 
> *(HINT: use the biological name of the tiger)*

```
SELECT ncbi_id, species, tax_string, tree_display_name, align_display_name
FROM Rfam.taxonomy
WHERE species = "Panthera tigris sumatrae (Sumatran tiger)";
```


### Q3. Find all the columns that can be used to connect the tables in the given database. 

```
SELECT
TABLE_NAME AS TABLE_1,
REFERENCED_TABLE_NAME AS 'TABLE_2 (reference table)',
COLUMN_NAME AS 'TABLE_1 columns',
REFERENCED_COLUMN_NAME AS 'TABLE_2 columns (reference table)'
FROM information_schema.key_column_usage
WHERE referenced_table_name IS NOT NULL -- it filters out any records that don't have a connection to another table
```


### Q4. Which type of rice has the longest DNA sequence? 
> *(HINT: use the rfamseq and the taxonomy tables)*

```
SELECT r.length as 'DNA Length', t.species as Species 
FROM rfamseq r
INNER JOIN taxonomy t ON t.ncbi_id = r.ncbi_id 
WHERE r.length = 
(
    SELECT MAX(length) 
    FROM rfamseq
);
```


### Q5. We want to paginate a list of the family names and their longest DNA sequence lengths (in descending order of length) where only families that have DNA sequence lengths greater than 1,000,000 are included. Give a query that will return the 9th page when there are 15 results per page.
> *(HINT: we need the family accession ID, family name and the maximum length in the results)*

```
SELECT f.rfam_acc  as 'Family accession ID', w.title as 'Family Name', MAX(r.length) as DNA_Length
from family f , rfamseq r , full_region full_r , wikitext w 
WHERE 
f.auto_wiki = w.auto_wiki and
f.rfam_acc = full_r.rfam_acc and
full_r.rfamseq_acc = r.rfamseq_acc
GROUP by f.rfam_acc, w.title
having DNA_Length > 1000000
ORDER by DNA_Length desc
LIMIT 15 OFFSET 120; -- 9th page with 15 results per page (8 pages * 15 results = 120 results skipped);
```


