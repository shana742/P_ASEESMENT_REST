# from django.shortcuts import render

# # Create your views here.

# # blog/views.py
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import BlogPost, Comment
# from .serializers import BlogPostSerializer, CommentSerializer
# from django.shortcuts import redirect

# def redirect_to_api(request):
#     return redirect('/api/blogs/')


# @api_view(['GET', 'POST'])
# def blog_list(request):
#     if request.method == 'GET':
#         posts = BlogPost.objects.all()
#         serializer = BlogPostSerializer(posts, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = BlogPostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# @api_view(['GET', 'PUT', 'DELETE'])
# def blog_detail(request, pk):
#     try:
#         post = BlogPost.objects.get(pk=pk)
#     except BlogPost.DoesNotExist:
#         return Response({'error': 'Post not found'}, status=404)

#     if request.method == 'GET':
#         serializer = BlogPostSerializer(post)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = BlogPostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         post.delete()
#         return Response({'message': 'Post deleted'}, status=204)


from rest_framework import viewsets
from .models import BlogPost, Comment
from .serializers import BlogPostSerializer, CommentSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
