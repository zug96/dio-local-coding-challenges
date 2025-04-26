using System;
// Importar CultureInfo para garantir o uso do ponto como separador decimal na leitura
using System.Globalization;

public class Desafio
{
  public static void Main()
  {
	//Lê os valores de Entrada:
	// Usar CultureInfo.InvariantCulture para garantir que Parse espera '.' como separador decimal
	float valorSalario = float.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
	float valorBeneficios = float.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);

	// Correção: Inicializar com float literal
	float valorImposto = 0.0f;
	
	// Correção: Usar && para o operador E lógico
	if (valorSalario >= 0 && valorSalario <= 1100)
	{ 
	   // Atribui a alíquota de 5% mediante o salário:
	   valorImposto = 0.05f * valorSalario;
	} 
	else if (valorSalario >= 1100.01 && valorSalario <= 2500.00)
	{
	  valorImposto = 0.10f * valorSalario;
	} 
	else // Para salários > 2500.00
	{
	   valorImposto = 0.15f * valorSalario;
	}

	//Calcula e imprime a Saída (com 2 casas decimais):
	float saida = valorSalario - valorImposto + valorBeneficios;
	Console.WriteLine(saida.ToString("0.00", CultureInfo.InvariantCulture));
  }
}
