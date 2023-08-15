#include "lists.h"
/**
 * is_palindrome - chek if linked list is a palindrome
 * @head: the head of the linked list
 * Return: 1 if the list palindrome or 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *new_head = (*head);
	int array_int[1024];
	int count = 0, middle;

	if (!head || !(*head))
		return (1);
	while (new_head)
	{
		count++;
		new_head = new_head->next;
	}
	new_head = (*head);
	count = 0;
	while (new_head)
	{
		array_int[count] = new_head->n;
		new_head = new_head->next;
		count++;
	}
	count--;
	middle = count;
	count = 0;
	while (count < middle)
	{
		if (array_int[count] != array_int[middle])
			return (0);
		count++, middle--;
	}
	return (1);
}
