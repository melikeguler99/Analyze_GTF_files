# GTF to BED converter in Python
gtf_file = 'Homo_sapiens.GRCh38.99.gtf'
bed_file = 'output2.bed'

with open(gtf_file, 'r') as gtf, open(bed_file, 'w') as bed:
    for line in gtf:
        if line.startswith('#'):
            continue
        fields = line.strip().split('\t')
        chromosome = fields[0]
        start = int(fields[3])
        features = fields[2]
        end = fields[4]
        strand = fields[6]
        bed_line = '\t'.join([chromosome, str(start), end, '.','.' , strand,features]) + '\n'
        bed.write(bed_line)# GTF to BED converter in Python
gtf_file = 'Homo_sapiens.GRCh38.99.gtf'
bed_file = 'output2.bed'

with open(gtf_file, 'r') as gtf, open(bed_file, 'w') as bed:
    for line in gtf:
        if line.startswith('#'):
            continue
        fields = line.strip().split('\t')
        chromosome = fields[0]
        start = int(fields[3])
        features = fields[2]
        end = fields[4]
        strand = fields[6]
        bed_line = '\t'.join([chromosome, str(start), end, '.','.' , strand,features]) + '\n'
        bed.write(bed_line)



# extract wanted regions from bed file
bed_file = 'output2.bed'
exon_file = 'exon_regions.bed'
five_prime_utr_file = 'five_prime_utr_regions.bed'
three_prime_utr_file = 'three_prime_utr_regions.bed'

with open(bed_file, 'r') as bed:
    exon_out = open(exon_file, 'w')
    five_prime_utr_out = open(five_prime_utr_file, 'w')
    three_prime_utr_out = open(three_prime_utr_file, 'w')

    for line in bed:
        fields = line.strip().split('\t')
        region_type = fields[6]

        if region_type == 'exon':
            exon_out.write(line)
        elif region_type == 'five_prime_utr':
            five_prime_utr_out.write(line)
        elif region_type == 'three_prime_utr':
            three_prime_utr_out.write(line)

    exon_out.close()
    five_prime_utr_out.close()
    three_prime_utr_out.close()# extract wanted regions from bed file
bed_file = 'output2-3.bed'
exon_file = 'exon_regions.bed'
five_prime_utr_file = 'five_prime_utr_regions.bed'
three_prime_utr_file = 'three_prime_utr_regions.bed'

with open(bed_file, 'r') as bed:
    exon_out = open(exon_file, 'w')
    five_prime_utr_out = open(five_prime_utr_file, 'w')
    three_prime_utr_out = open(three_prime_utr_file, 'w')

    for line in bed:
        fields = line.strip().split('\t')
        region_type = fields[6]

        if region_type == 'exon':
            exon_out.write(line)
        elif region_type == 'five_prime_utr':
            five_prime_utr_out.write(line)
        elif region_type == 'three_prime_utr':
            three_prime_utr_out.write(line)

    exon_out.close()
    five_prime_utr_out.close()
    three_prime_utr_out.close()

