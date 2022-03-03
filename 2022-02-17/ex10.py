debito=float(input('Digite valor debito'))
credito=float(input('Digite valor credito'))

print('{} {}'.format(debito-credito, 'POSITIVO' if debito-credito>=0 else 'NEGATIVO'))