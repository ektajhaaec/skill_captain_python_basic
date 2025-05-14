# import asyncio

# async def pizza_delivery(customer):
#     print(f"Pizza ready to deliover for {customer}")
#     await  asyncio.sleep(3)
#     print(f"Pizza delivered to {customer}")

# async def  main():
#     customer_list = ["ekta","sagar", "puchka", "billu"]
#     task_list =[pizza_delivery(customer) for customer in customer_list]
#     await asyncio.gather(*task_list)

# asyncio.run(main())


import asyncio
async def countdown(n):
    
    await asyncio.sleep(3)
    print(f"{n}")

async def main() :
    n = int(input("Enter a number"))
    n= int(n)
    for i in range(n ,0,-1):
        await countdown(i)

asyncio.run(main())

    

