	addu $t0 $a0 $0
	bitpal $t1 $t0
	bne $t1 $0 exit
loop:
	lfsr $t0 $t0
	beq $t0 $a0 exit
	bitpal $t1 $t0
	bne $t1 $0 exit
	j loop
exit:
	addu $v0 $t0 $0
	jr $ra
	
