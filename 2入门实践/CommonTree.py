#coding=utf-8
'''
@description:无限级分类
@author:chenwei
@date:2016-07-12
'''
class CommonTree:
    def __init__(self):
        self.data           = {}
        self.info           = {}
        self.item           = {}
        self.cateArray      = {}
        self.statusField    = 'categories_status'
        self.parentIdField  = 'parent_id'
        self.preStr         ='&nbsp;&nbsp;'
    '''
    @description:设置节点内容
    '''
    def setNode(self,itemid, parent, value,info={}):
            itemid = int(itemid)
            parent = (int(parent) if int(parent) > 0 else 0)  
            self.data[itemid] = value
            if not info.has_key(self.statusField):
                info[self.statusField] = 1
            
            self.info[itemid] = info
            self.cateArray[itemid] = parent
    '''
    @description:判断某一个节点下面是否还有别的子节点
    @return:bool
    '''
    def hasChildren(self,itemid=0):
            itemid = int(itemid)
            for (k, v) in self.cateArray.items():
                if(v==itemid):
                    return True
            return False
    '''
    @description: 获取某一个节点下的子节点
    @param int
    @return Dict
    '''
    def getChilds(self,id=0):
        id = int(id)
        childArray={}
        childs=self.getChild(id)

        #包含当前节点。
        if id !=0:
            childArray[id] = id
        for (k, v) in childs.items():
            childArray[v]=v
            childArray.update(self.getChilds(v))
        return childArray
    '''
    @description: 获取某一个id的信息
    @param int
    @return Dict
    '''
    def getChild(self,id):
        id = int(id)
        childs    ={}
        for (k, v) in self.cateArray.items():
            if int(v)==id:
                #childs.update({k:k})
                childs[k]=k
        return childs
    '''
    @description:单线获取父节点
    '''
    def getNodeLever(self,id):
        id = int(id)
        if not vars().has_key('parentsList'):
            parentsList=[]
        if self.cateArray.has_key(self.cateArray[id]):
            parentsList.append(self.cateArray[id])
            parentsList.extend(self.getNodeLever(self.cateArray[id]))
        return parentsList

    '''
    @description:返回带缩进格式的字符串
    @return:string
    '''
    def getLayer(self,id):
        id = int(id)
        return  self.preStr * len(self.getNodeLever(id))
    '''
    @description:获取分类名称
    '''
    def getValue(self,id):
        id = int(id)
        return self.data[id]
    '''
    #返回某个id子分类下的数据,0是根分类
    #selected是选中的编号
    #return_array是否返回字典，如果不是则返回字符串<option value="......">......</option>
    #level 保留多少级 0 表示不限制
    #is_show_all是否显示所有子分类
    #@return:string or dict
    '''
    def getAllData(self,id ,selected, return_array= True,level=0,is_show_all=True):
        id = int(id)
        result = self.getChilds(id)
        if len(result)>0 :
            for (k, v) in result.items():
                dict={}
                dict['id']                   = v
                dict['data']                 = self.data[k]
                dict['level'] = len(self.getNodeLever(v))
                dict['has_children']         = self.hasChildren(v)
                self.item[v]                 = dict
                '''
                if self.info[v][self.parentIdField]:
                    self.item[v][self.parentIdField] = self.info[v][self.parentIdField]
                '''
                self.item[v]['info'] = self.info[v]
            #大于这个分类的将被删除
            children_level = 99999 

            if is_show_all == False :
                for (key, it) in self.item.items():
                    if it['level'] > children_level:
                        del(self.item[key])
                    else:
                        #如果不全部显示，跳过不显示的元素
                        if not it['info'][self.statusField]:

                            del(self.item[key]);

                        if children_level > it['level']:

                            children_level = it['level'] #标记一下，这样子分类也能删除
                        else:
                            children_level = 99999 #恢复初始值


            #截取到指定的缩减级别

            if level > 0 :
                if (id == 0):
                    end_level = level
                else:
                    copyd = self.item
                    for (k,v) in copyd.items():
                        if v:
                            first_item = v
                            break
                    end_level  = first_item['level'] + level
                #保留level小于end_level的部分
                for (key, val) in self.item.items():
                    if (val['level'] >= end_level):
                        del(self.item[key])
            if return_array :
                return self.item
            else:
                result_str = ''
                html_list=[]
                for (hkey, v) in self.item.items():
                    if v['id'] != selected :
                        strh = '<option value="'+str(v['id'])+'">'+self.preStr*int(v['level'])+v['data']+'</option>'+"\n"
                    else:
                        strh = '<option value="'+str(v['id'])+'" selected="selected">'+self.preStr*int(v['level'])+v['data']+'</option>'+"\n"
                    html_list.append(strh)
                result_str = ''.join(html_list)
                return result_str
        else:

            return False
        



'''
开始实例化类,执行测试
'''
tree = CommonTree()
lists = {}
lists[0]={'id':'10','name':'A','parent_id':'0','info':{'categories_status':'1','mark':'101010'}}
lists[1]={'id':'11','name':'A1','parent_id':'10','info':{'categories_status':'0','mark':'111111'}}
lists[2]={'id':'12','name':'A2','parent_id':'11','info':{'categories_status':'0','mark':'121212'}}
lists[3]={'id':'13','name':'B1','parent_id':'0','info':{'categories_status':'1','mark':'131313'}}
lists[4]={'id':'14','name':'B2','parent_id':'13','info':{'categories_status':'1','mark':'141414'}}
info = []
for (k, v) in lists.items():
    tree.setNode(v['id'],v['parent_id'],v['name'],v['info'])
print lists
print "\n"
print tree.getChilds('10')
print tree.getChilds('13')
print tree.hasChildren('14')
print tree.cateArray
print tree.getNodeLever('13')
print tree.getValue('13')
print tree.getLayer('14')
#显示分类字符串
print tree.getAllData('10','14',False)
#显示分类字典
print tree.getAllData('10','14',True)
'''
运行结果
{0: {'categories_status': '1', 'parent_id': 0, 'id': 10, 'name': 'A'}, 1: {'categories_status': '1', 'parent_id': 10, 'id': 11, 'name': 'A1'}, 2: {'categories_status': '1', 'parent_id': 11, 'id': 12, 'name': 'A2'}, 3: {'categories_status': '1', 'parent_id': 0, 'id': 13, 'name': 'B1'}, 4: {'categories_status': '1', 'parent_id': 13, 'id': 14, 'name': 'B2'}}


{10: 10, 11: 11, 12: 12}
{13: 13, 14: 14}
False
{10: 0, 11: 10, 12: 11, 13: 0, 14: 13}
[]
B1
&nbsp;&nbsp;
<option value="10">A</option>
<option value="11">&nbsp;&nbsp;A1</option>
<option value="12">&nbsp;&nbsp;&nbsp;&nbsp;A2</option>
'''