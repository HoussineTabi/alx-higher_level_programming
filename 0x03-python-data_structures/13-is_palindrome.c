#include "lists.h"
/**
 * is_palindrome - chek if linked list is a palindrome
 * @head: the head of the linked list
 * Return: 1 if the list palindrome or 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *new_head = (*head);
	int *array_int;
	int count = 0, middle;

	if (!head || !(*head))
		return (1);
	while (new_head)
	{
		count++;
		new_head = new_head->next;
	}
	new_head = *head;
	new_head = inverse_linked_list(&new_head, new_head)
	array_int = malloc(sizeof(int) * count);
	if (!array_int)
		return (0);
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
/**
 * inverse_linked_list - is a funciton that inverse a linkedlist
 * @head: the adress of head of the list
 */

listint_t *inverse_linked_list(listint_t **head, listint_t *new_head)
{
	listint_t *helper = NULL;

	if (!(head) || !(*head))
		return (NULL);
	if (new_head->next == NULL)
	{
		new_head->next = (*head);
		(*head) = new_head;
		return (*head);
	}
	inverse_linked_list(&((*head)->next), *head);





