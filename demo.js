// ═══════════════════════════════════════════════════════
//  CRONUX-CRX Demo — datos del wizard igual que la app
// ═══════════════════════════════════════════════════════

const CATS = [
  {id:'software',      label:'Software',      icon:'terminal',     color:'#22d3ee', bg:'#EEF2FF', sub:true },
  {id:'documentos',    label:'Documentos',    icon:'file-text',    color:'#48BB78', bg:'#F0FFF4', sub:true },
  {id:'imagenes',      label:'Imágenes',      icon:'image',        color:'#ED8936', bg:'#FFF7ED', sub:true },
  {id:'tareas',        label:'Tareas',        icon:'check-square', color:'#F56565', bg:'#FFF5F5', sub:false},
  {id:'investigacion', label:'Investigación', icon:'microscope',   color:'#38B2AC', bg:'#E6FFFA', sub:false},
  {id:'diseno',        label:'Diseño',        icon:'brush',        color:'#9F7AEA', bg:'#FAF5FF', sub:false},
];

const TECHS = [
  {id:'javascript',label:'JavaScript',img:'img/icons/javascript.png',color:'#F7DF1E',bg:'#FFFBEA',sub:true },
  {id:'python',    label:'Python',    img:'img/icons/python.png',    color:'#4299E1',bg:'#EBF8FF',sub:false},
  {id:'java',      label:'Java',      img:'img/icons/java.png',      color:'#ED8936',bg:'#FFFAF0',sub:false},
  {id:'php',       label:'PHP',       img:'img/icons/php.png',       color:'#8892BF',bg:'#F3F4F6',sub:false},
  {id:'ruby',      label:'Ruby',      img:'img/icons/ruby.png',      color:'#F56565',bg:'#FFF5F5',sub:false},
  {id:'go',        label:'Go',        img:'img/icons/go.png',        color:'#38B2AC',bg:'#E6FFFA',sub:false},
  {id:'flutter',   label:'Flutter',   img:'img/icons/flutter.png',   color:'#02569B',bg:'#E3F2FD',sub:false},
  {id:'dotnet',    label:'.NET',      img:'img/icons/dotnet.png',    color:'#9F7AEA',bg:'#FAF5FF',sub:false},
  {id:'general',   label:'General',   img:'img/icons/lanzamiento-del-proyecto.png', color:'#718096',bg:'#F7FAFC',sub:false},
];

const JS_SUBS = [
  {id:'react',     label:'React',     img:'img/icons/react.png',      color:'#0891B2',bg:'#E0F2FE'},
  {id:'vanilla_js',label:'Vanilla JS',img:'img/icons/javascript.png', color:'#F7DF1E',bg:'#FFFBEA'},
  {id:'nodejs',    label:'Node.js',   img:'img/icons/node.png',       color:'#68D391',bg:'#F0FFF4'},
  {id:'general_js',label:'General',   img:'img/icons/lanzamiento-del-proyecto.png', color:'#718096',bg:'#F7FAFC'},
];

const DOC_SUBS = [
  {id:'word',       label:'Word',       img:'img/icons/word.png',       color:'#2B579A',bg:'#E3F2FD'},
  {id:'excel',      label:'Excel',      img:'img/icons/excel.png',      color:'#217346',bg:'#E8F5E9'},
  {id:'powerpoint', label:'PowerPoint', img:'img/icons/powerpoint.png', color:'#D24726',bg:'#FFEBEE'},
  {id:'pdf',        label:'PDF',        img:'img/icons/pdf.png',        color:'#F40F02',bg:'#FFEBEE'},
  {id:'latex',      label:'LaTeX',      img:'img/icons/latex.png',      color:'#008080',bg:'#E0F2F1'},
  {id:'general_doc',label:'General',    img:'img/icons/lanzamiento-del-proyecto.png', color:'#718096',bg:'#F7FAFC'},
];

const IMG_SUBS = [
  {id:'png',        label:'PNG', img:'img/icons/png.png', color:'#10B981',bg:'#ECFDF5'},
  {id:'jpg',        label:'JPG', img:'img/icons/jpg.png', color:'#F59E0B',bg:'#FEF3C7'},
  {id:'svg',        label:'SVG', img:'img/icons/svg.png', color:'#8B5CF6',bg:'#F3E8FF'},
  {id:'gif',        label:'GIF', img:'img/icons/gif.png', color:'#EC4899',bg:'#FCE7F3'},
  {id:'raw',        label:'RAW', img:'img/icons/raw.png', color:'#6366F1',bg:'#EEF2FF'},
  {id:'general_img',label:'General',img:'img/icons/lanzamiento-del-proyecto.png', color:'#718096',bg:'#F7FAFC'},
];

// Mapa de iconos PNG por tipo
const TYPE_IMG = {
  python:'img/icons/python.png', javascript:'img/icons/javascript.png',
  java:'img/icons/java.png', php:'img/icons/php.png', ruby:'img/icons/ruby.png',
  go:'img/icons/go.png', flutter:'img/icons/flutter.png', dotnet:'img/icons/dotnet.png',
  react:'img/icons/react.png', vanilla_js:'img/icons/javascript.png',
  nodejs:'img/icons/node.png', word:'img/icons/word.png', excel:'img/icons/excel.png',
  powerpoint:'img/icons/powerpoint.png', pdf:'img/icons/pdf.png', latex:'img/icons/latex.png',
  general:'img/icons/lanzamiento-del-proyecto.png',
  general_js:'img/icons/lanzamiento-del-proyecto.png',
  general_doc:'img/icons/lanzamiento-del-proyecto.png',
  general_img:'img/icons/lanzamiento-del-proyecto.png',
};
const TYPE_LUCIDE = {
  tareas:'check-square', investigacion:'microscope', diseno:'brush',
  general:'folder', general_js:'folder', general_doc:'file-text', general_img:'image',
};
const TYPE_COLOR = {
  tareas:'#F56565', investigacion:'#38B2AC', diseno:'#9F7AEA',
  general:'#22d3ee', general_js:'#718096', general_doc:'#48BB78', general_img:'#ED8936',
};

function iconHtml(type, size) {
  size = size || 48;
  const img = TYPE_IMG[type];
  if (img) return '<img src="'+img+'" width="'+size+'" height="'+size+'" style="object-fit:contain">';
  const ic = TYPE_LUCIDE[type] || 'folder';
  const col = TYPE_COLOR[type] || '#22d3ee';
  const s = Math.round(size * 0.7);
  return '<i data-lucide="'+ic+'" style="width:'+s+'px;height:'+s+'px;color:'+col+'"></i>';
}

// Datos de ejemplo
const SAMPLE = [
  {id:1, name:'Tesis Universidad', type:'word',
   path:'/home/usuario/Documentos/Tesis', created:'2026-04-10 09:00',
   versions:[
     {v:'1.3',date:'Hace 2 días',   msg:'Correcciones capítulo 3', files:12,size:'2.4 MB'},
     {v:'1.2',date:'Hace 5 días',   msg:'Metodología agregada',    files:11,size:'2.1 MB'},
     {v:'1.1',date:'Hace 1 semana', msg:'Revisión introducción',   files:10,size:'1.9 MB'},
     {v:'1',  date:'Hace 2 semanas',msg:'Versión inicial',         files: 8,size:'1.5 MB'},
   ]},
  {id:2, name:'API REST Node', type:'nodejs',
   path:'/home/usuario/Proyectos/api-rest', created:'2026-03-15 11:00',
   versions:[
     {v:'1.2',date:'Hace 3 horas', msg:'Autenticación JWT', files:24,size:'1.1 MB'},
     {v:'1.1',date:'Ayer',         msg:'CRUD de usuarios',  files:20,size:'0.9 MB'},
     {v:'1',  date:'Hace 1 semana',msg:'Versión inicial',   files:15,size:'0.7 MB'},
   ]},
];

// ═══════════════════════════════════════════════════════
//  APP OBJECT
// ═══════════════════════════════════════════════════════
const app = (function() {

  // ── estado ──────────────────────────────────────────
  let projects = [];
  let current  = null;
  let view     = 'versiones';
  let pendingFn = null;
  let editingId = null;

  // wizard
  let wStep = 'cat';
  let wCat=null, wTech=null, wSub=null;

  // ── init ─────────────────────────────────────────────
  function init() {
    projects = JSON.parse(JSON.stringify(SAMPLE));
    lucide.createIcons();
    renderHome();
  }

  // ── helpers de pantalla ──────────────────────────────
  function show(id) {
    ['homeScreen','wizardScreen','projectScreen'].forEach(function(s){
      document.getElementById(s).style.display = (s===id) ? 'flex' : 'none';
    });
  }

  // ── HOME ─────────────────────────────────────────────
  function renderHome() {
    var list = document.getElementById('projectsList');
    list.innerHTML = '';

    if (!projects.length) {
      document.getElementById('emptyState').style.display = 'flex';
      document.getElementById('projectsSection').style.display = 'none';
      show('homeScreen');
      lucide.createIcons();
      return;
    }

    document.getElementById('emptyState').style.display = 'none';
    document.getElementById('projectsSection').style.display = 'block';

    projects.forEach(function(p) {
      var card = document.createElement('div');
      card.className = 'proj-card';
      card.innerHTML =
        '<div class="proj-card-ico">'+iconHtml(p.type,48)+'</div>'+
        '<div class="proj-card-info">'+
          '<div class="proj-card-name">'+p.name+'</div>'+
          '<div class="proj-card-path">'+
            '<i data-lucide="folder" style="width:13px;height:13px"></i> '+p.path+
          '</div>'+
        '</div>'+
        '<div class="proj-card-acts" onclick="event.stopPropagation()">'+
          '<button class="act-btn edit"   title="Editar nombre"  onclick="app.openEditName('+p.id+')"><i data-lucide="pencil"></i></button>'+
          '<button class="act-btn folder" title="Abrir carpeta"  onclick="app.toast(\'✓ Carpeta abierta\')"><i data-lucide="folder-open"></i></button>'+
          '<button class="act-btn export" title="Exportar"       onclick="app.toast(\'✓ Proyecto exportado\')"><i data-lucide="download"></i></button>'+
          '<button class="act-btn del"    title="Eliminar"       onclick="app.openDelProj('+p.id+')"><i data-lucide="trash-2"></i></button>'+
        '</div>';
      card.addEventListener('click', function(){ openProject(p.id); });
      list.appendChild(card);
    });

    show('homeScreen');
    lucide.createIcons();
  }

  function goHome() {
    current = null;
    renderHome();
  }

  function search(q) {
    q = q.toLowerCase();
    document.querySelectorAll('.proj-card').forEach(function(c, i) {
      var p = projects[i];
      c.style.display = (p.name.toLowerCase().includes(q) || p.path.toLowerCase().includes(q)) ? 'flex' : 'none';
    });
  }

  function cleanProjects() {
    toast('✓ Lista actualizada, sin cambios');
  }

  // ── WIZARD ───────────────────────────────────────────
  function showWizard() {
    wStep='cat'; wCat=null; wTech=null; wSub=null;
    renderWizard();
    show('wizardScreen');
  }

  function closeWizard() {
    renderHome();
  }

  function renderWizard() {
    var el = document.getElementById('wizardContent');
    if      (wStep==='cat')    el.innerHTML = buildCat();
    else if (wStep==='tech')   el.innerHTML = buildTech();
    else if (wStep==='jssub')  el.innerHTML = buildSub('JavaScript', JS_SUBS, 'tech');
    else if (wStep==='docsub') el.innerHTML = buildSub('Documentos', DOC_SUBS, 'cat');
    else if (wStep==='imgsub') el.innerHTML = buildSub('Imágenes',   IMG_SUBS, 'cat');
    else if (wStep==='form')   el.innerHTML = buildForm();
    lucide.createIcons();
  }

  function buildCat() {
    var cards = CATS.map(function(c) {
      return '<div class="wiz-cat-card" onclick="app._selectCat(\''+c.id+'\')">'+
        '<div class="wiz-cat-ico" style="background:'+c.bg+';color:'+c.color+'">'+
          '<i data-lucide="'+c.icon+'"></i>'+
        '</div>'+
        '<span>'+c.label+'</span>'+
      '</div>';
    }).join('');
    return '<div class="wiz-screen">'+
      '<button class="wiz-back" onclick="app.closeWizard()"><i data-lucide="arrow-left"></i></button>'+
      '<div class="wiz-body">'+
        '<h1 class="wiz-title">¿Qué tipo de proyecto es?</h1>'+
        '<div class="wiz-grid-3">'+cards+'</div>'+
      '</div>'+
    '</div>';
  }

  function _selectCat(id) {
    wCat = CATS.find(function(c){return c.id===id;});
    if      (id==='software')   { wStep='tech';   }
    else if (id==='documentos') { wStep='docsub'; }
    else if (id==='imagenes')   { wStep='imgsub'; }
    else                        { wStep='form';   }
    renderWizard();
  }

  function buildTech() {
    var main = TECHS.slice(0,8).map(function(t) {
      return '<div class="wiz-tech-card" onclick="app._selectTech(\''+t.id+'\')">'+
        '<div class="wiz-tech-ico" style="background:'+t.bg+'">'+
          (t.img ? '<img src="'+t.img+'" width="56" height="56" style="object-fit:contain">' : '<i data-lucide="folder" style="color:'+t.color+'"></i>')+
        '</div>'+
        '<span>'+t.label+'</span>'+
      '</div>';
    }).join('');
    var gen = '<div class="wiz-tech-card gen" onclick="app._selectTech(\'general\')">'+
      '<div class="wiz-tech-ico" style="background:#F7FAFC"><i data-lucide="folder" style="color:#718096"></i></div>'+
      '<span>General</span></div>';
    return '<div class="wiz-screen">'+
      '<button class="wiz-back" onclick="app._wBack(\'cat\')"><i data-lucide="arrow-left"></i></button>'+
      '<div class="wiz-body">'+
        '<div class="wiz-badge" style="background:#EEF2FF;color:#22d3ee"><i data-lucide="terminal"></i> Software</div>'+
        '<h1 class="wiz-title">Selecciona tu tecnología</h1>'+
        '<p class="wiz-sub">Elige la tecnología para tu proyecto de software</p>'+
        '<div class="wiz-tech-layout"><div class="wiz-grid-4">'+main+'</div>'+gen+'</div>'+
      '</div>'+
    '</div>';
  }

  function _selectTech(id) {
    wTech = TECHS.find(function(t){return t.id===id;});
    wStep = (id==='javascript') ? 'jssub' : 'form';
    renderWizard();
  }

  function buildSub(label, items, backStep) {
    var cards = items.map(function(s) {
      return '<div class="wiz-sub-card" onclick="app._selectSub(\''+s.id+'\')">'+
        '<div class="wiz-sub-ico" style="background:'+s.bg+'">'+
          (s.img ? '<img src="'+s.img+'" width="52" height="52">' : '<i data-lucide="file" style="color:'+s.color+';width:36px;height:36px"></i>')+
        '</div>'+
        '<span>'+s.label+'</span>'+
      '</div>';
    }).join('');
    return '<div class="wiz-screen">'+
      '<button class="wiz-back" onclick="app._wBack(\''+backStep+'\')"><i data-lucide="arrow-left"></i></button>'+
      '<div class="wiz-body">'+
        '<h1 class="wiz-title">¿Qué tipo de '+label.toLowerCase()+'?</h1>'+
        '<p class="wiz-sub">Elige el formato específico para tu proyecto</p>'+
        '<div class="wiz-grid-3">'+cards+'</div>'+
      '</div>'+
    '</div>';
  }

  function _selectSub(id) {
    var all = JS_SUBS.concat(DOC_SUBS).concat(IMG_SUBS);
    wSub = all.find(function(s){return s.id===id;});
    wStep = 'form';
    renderWizard();
  }

  function _wBack(step) {
    wStep = step;
    renderWizard();
  }

  function buildForm() {
    var ft = wSub || wTech || wCat;
    var ico = ft.img
      ? '<img src="'+ft.img+'" width="64" height="64">'
      : '<i data-lucide="'+(ft.icon||'folder')+'" style="color:'+ft.color+';width:48px;height:48px"></i>';
    var backStep = wSub ? (wCat && wCat.id==='software' ? 'jssub' : wCat && wCat.id==='documentos' ? 'docsub' : 'imgsub') : (wTech ? 'tech' : 'cat');
    return '<div class="wiz-screen">'+
      '<button class="wiz-back" onclick="app._wBack(\''+backStep+'\')"><i data-lucide="arrow-left"></i></button>'+
      '<div class="wiz-form-layout">'+
        '<div class="wiz-form-left">'+
          '<h1 class="wiz-title" style="font-size:26px">Nuevo Proyecto</h1>'+
          '<p class="wiz-sub">Ingresa el nombre de tu proyecto</p>'+
          '<div class="field" style="margin-top:32px">'+
            '<label>Nombre del proyecto</label>'+
            '<input type="text" id="wizName" placeholder="mi-proyecto-increible" autofocus>'+
          '</div>'+
          '<div class="field">'+
            '<label>Tipo detectado</label>'+
            '<div class="type-badge" style="background:'+(ft.bg||'#EEF2FF')+';color:'+(ft.color||'#22d3ee')+'">'+ft.label+'</div>'+
          '</div>'+
        '</div>'+
        '<div class="wiz-form-right">'+
          '<div class="wiz-proj-ico" style="background:'+(ft.bg||'#EEF2FF')+'">'+ico+'</div>'+
          '<p class="wiz-proj-lbl">Proyecto</p>'+
          '<button class="btn-primary lg" style="width:280px;margin-top:48px" onclick="app.createProject()">'+
            '<i data-lucide="rocket"></i> Crear Proyecto'+
          '</button>'+
        '</div>'+
      '</div>'+
    '</div>';
  }

  function createProject() {
    var name = (document.getElementById('wizName')||{}).value;
    if (!name || !name.trim()) { toast('Escribe un nombre','error'); return; }
    name = name.trim();
    var ft = wSub || wTech || wCat;
    var p = {
      id: Date.now(), name: name, type: ft.id,
      path: '/home/usuario/Proyectos/'+name.toLowerCase().replace(/\s+/g,'-'),
      created: new Date().toLocaleString('es-MX'),
      versions: [{v:'1',date:'Ahora',msg:'Versión inicial',files:0,size:'0 B'}]
    };
    projects.push(p);
    renderHome();
    toast('✓ Proyecto "'+name+'" creado');
    setTimeout(function(){ openProject(p.id); }, 400);
  }

  // ── PROJECT ──────────────────────────────────────────
  function openProject(id) {
    current = projects.find(function(p){return p.id===id;});
    if (!current) return;
    document.getElementById('projName').textContent = current.name;
    document.getElementById('projPath').textContent = current.path;
    document.getElementById('projIco').innerHTML = iconHtml(current.type, 28);
    view = 'versiones';
    updateDock();
    renderProjBody();
    show('projectScreen');
    lucide.createIcons();
  }

  function switchView(v) {
    view = v;
    updateDock();
    renderProjBody();
  }

  function updateDock() {
    document.querySelectorAll('.dock-btn').forEach(function(b){
      b.classList.toggle('active', b.dataset.view===view);
    });
  }

  function renderProjBody() {
    var el = document.getElementById('projBody');
    el.innerHTML = (view==='versiones') ? buildVersionsView() : buildStatsView();
    lucide.createIcons();
  }

  function buildVersionsView() {
    var vs = current.versions;
    if (!vs.length) return '<div class="empty-ver"><div class="empty-ver-ico"><i data-lucide="layers"></i></div><h3>No hay versiones</h3><p>Guarda tu primera versión para comenzar</p></div>';
    var maxV = Math.max.apply(null, vs.map(function(v){return parseFloat(v.v);}));
    var cards = vs.map(function(v,i){return buildVerCard(v,i,maxV);}).join('');
    return '<div class="ver-scroll"><div class="ver-hdr"><i data-lucide="layers" style="color:#22d3ee;width:20px;height:20px"></i><span>'+vs.length+' Versión'+(vs.length!==1?'es':'')+'</span></div><div class="ver-list">'+cards+'</div></div>';
  }

  function buildVerCard(v, idx, maxV) {
    var isCur  = idx===0;
    var isLast = parseFloat(v.v)===maxV && !isCur;
    var curBadge  = isCur  ? '<span class="badge red"><i data-lucide="check-circle" style="width:12px;height:12px"></i> ACTUAL</span>' : '';
    var lastBadge = isLast ? '<span class="badge blue"><i data-lucide="star" style="width:12px;height:12px"></i> ÚLTIMA</span>' : '';
    return '<div class="ver-card'+(isCur?' current':'')+'">'+
      '<div class="ver-hdr-row">'+
        '<div class="ver-badge"><i data-lucide="tag" style="width:16px;height:16px;color:#22d3ee"></i><span>v'+v.v+'</span></div>'+
        curBadge+lastBadge+
        '<div style="flex:1"></div>'+
        '<div class="ver-date"><i data-lucide="clock" style="width:13px;height:13px"></i>'+v.date+'</div>'+
      '</div>'+
      '<div class="ver-msg">'+v.msg+'</div>'+
      '<div class="ver-stats">'+
        '<span class="stat-pill green"><i data-lucide="file-text" style="width:14px;height:14px"></i>'+v.files+' archivo'+(v.files!==1?'s':'')+'</span>'+
        '<span class="stat-pill yellow"><i data-lucide="folder" style="width:14px;height:14px"></i>'+v.size+'</span>'+
      '</div>'+
      '<div class="ver-actions">'+
        '<button class="ver-btn primary" onclick="app.openRestore(\''+v.v+'\')"><i data-lucide="rotate-ccw"></i> Restaurar</button>'+
        '<button class="ver-btn outline" onclick="app.toast(\'Carpeta abierta\')"><i data-lucide="folder-open"></i> Abrir Carpeta</button>'+
        '<button class="ver-btn icon-red" onclick="app.openDelVer(\''+v.v+'\')"><i data-lucide="trash-2"></i></button>'+
      '</div>'+
    '</div>';
  }

  function buildStatsView() {
    var vs = current.versions;
    var totalFiles = vs.reduce(function(a,v){return a+v.files;},0);
    return '<div class="stats-scroll">'+
      '<div class="stats-cards">'+
        '<div class="stat-card blue"><div class="stat-ico"><i data-lucide="layers"></i></div><div class="stat-num">'+vs.length+'</div><div class="stat-lbl">Versiones Guardadas</div></div>'+
        '<div class="stat-card green"><div class="stat-ico"><i data-lucide="file-text"></i></div><div class="stat-num">'+totalFiles+'</div><div class="stat-lbl">Archivos Rastreados</div></div>'+
        '<div class="stat-card yellow"><div class="stat-ico"><i data-lucide="folder"></i></div><div class="stat-num">'+(vs[0]?vs[0].size:'0 B')+'</div><div class="stat-lbl">Tamaño Total</div></div>'+
      '</div>'+
      '<div class="info-card">'+
        '<h3>Información del Proyecto</h3>'+
        infoRow('label','Nombre',current.name)+
        infoRow('tag','Tipo',current.type.toUpperCase())+
        infoRow('folder-open','Ubicación',current.path)+
        infoRow('calendar','Creado',current.created)+
      '</div>'+
    '</div>';
  }

  function infoRow(icon, label, val) {
    return '<div class="info-row"><div class="info-ico"><i data-lucide="'+icon+'"></i></div><div><div class="info-lbl">'+label+'</div><div class="info-val">'+val+'</div></div></div>';
  }

  // ── MODALS ───────────────────────────────────────────
  function openModal(id) {
    document.getElementById(id).style.display = 'flex';
    lucide.createIcons();
  }

  function closeModal() {
    document.querySelectorAll('.backdrop').forEach(function(b){b.style.display='none';});
    pendingFn = null;
  }

  function closeModalOutside(e, id) {
    if (e.target === document.getElementById(id)) closeModal();
  }

  function confirmAction() {
    if (pendingFn) pendingFn();
  }

  function openRestore(v) {
    document.getElementById('restoreDesc').textContent = '¿Restaurar la versión v'+v+'?';
    pendingFn = function() {
      var idx = current.versions.findIndex(function(x){return x.v===v;});
      if (idx>0) { var x=current.versions.splice(idx,1)[0]; current.versions.unshift(x); }
      closeModal(); renderProjBody(); toast('✓ Versión v'+v+' restaurada');
    };
    openModal('restoreModal');
  }

  function openDelVer(v) {
    document.getElementById('delVerDesc').textContent = '¿Eliminar la versión v'+v+'?';
    pendingFn = function() {
      current.versions = current.versions.filter(function(x){return x.v!==v;});
      closeModal(); renderProjBody(); toast('✓ Versión v'+v+' eliminada');
    };
    openModal('delVerModal');
  }

  function openDelProj(id) {
    var p = projects.find(function(x){return x.id===id;});
    document.getElementById('delProjDesc').textContent = '¿Eliminar "'+p.name+'" y todas sus versiones?';
    pendingFn = function() {
      projects = projects.filter(function(x){return x.id!==id;});
      closeModal();
      if (current && current.id===id) goHome(); else renderHome();
      toast('✓ Proyecto eliminado');
    };
    openModal('delProjModal');
  }

  function openEditName(id) {
    editingId = id;
    var p = projects.find(function(x){return x.id===id;});
    document.getElementById('editNameInput').value = p.name;
    openModal('editNameModal');
  }

  function saveEditName() {
    var name = document.getElementById('editNameInput').value.trim();
    if (!name) { toast('El nombre no puede estar vacío','error'); return; }
    var p = projects.find(function(x){return x.id===editingId;});
    if (p) {
      p.name = name;
      if (current && current.id===editingId) {
        current.name = name;
        document.getElementById('projName').textContent = name;
      }
    }
    closeModal(); renderHome(); toast('✓ Nombre actualizado');
  }

  function saveVersion() {
    var msg = document.getElementById('versionMsg').value.trim();
    if (!msg) { toast('Escribe una descripción','error'); return; }
    var last = parseFloat(current.versions[0] ? current.versions[0].v : '1');
    var nv = (last+0.1).toFixed(1).replace(/\.0$/,'');
    current.versions.unshift({
      v:nv, date:'Ahora', msg:msg,
      files:(current.versions[0]?current.versions[0].files:0)+Math.floor(Math.random()*3),
      size:((parseFloat(current.versions[0]?current.versions[0].size:1)||1)+0.1).toFixed(1)+' MB'
    });
    closeModal();
    document.getElementById('versionMsg').value='';
    renderProjBody();
    toast('✓ Versión v'+nv+' guardada');
  }

  // ── TOAST ────────────────────────────────────────────
  function toast(msg, type) {
    var t = document.getElementById('toast');
    document.getElementById('toastMsg').textContent = msg;
    t.className = 'toast show' + (type==='error' ? ' error' : '');
    lucide.createIcons();
    setTimeout(function(){ t.className='toast'; }, 2500);
  }

  // ── API pública ──────────────────────────────────────
  return {
    init:init, goHome:goHome, search:search, cleanProjects:cleanProjects,
    showWizard:showWizard, closeWizard:closeWizard,
    _selectCat:_selectCat, _selectTech:_selectTech, _selectSub:_selectSub, _wBack:_wBack,
    createProject:createProject,
    switchView:switchView,
    openModal:openModal, closeModal:closeModal, closeModalOutside:closeModalOutside, confirmAction:confirmAction,
    openRestore:openRestore, openDelVer:openDelVer, openDelProj:openDelProj,
    openEditName:openEditName, saveEditName:saveEditName,
    saveVersion:saveVersion,
    toast:toast,
  };
})();

document.addEventListener('DOMContentLoaded', function(){ app.init(); });
